# -*- coding: utf-8 -*-
import requests
import scrapy
from lxml import etree
from scrapy.loader import ItemLoader

from EnglishSpider.items import MathItem
from EnglishSpider.spiders.utils.util import deal_erji_raw_str


class MathspiderSpider(scrapy.Spider):
    name = 'MathSpider'
    allowed_domains = ['tiku.21cnjy.com/tiku.php']
    start_urls = ['http://tiku.21cnjy.com/tiku.php/']

    def start_requests(self):

        _u = "http://tiku.21cnjy.com/tiku.php?mod=quest&channel=3&xd=3"

        resp = requests.get(url=_u)
        parser = etree.HTML(resp.text)

        urls = parser.xpath("//ul[@id='con_one_1']//a/@href")

        for u in urls:
            u = "http://tiku.21cnjy.com/tiku.php" + u
            yield scrapy.Request(url=u, callback=self.parse, dont_filter=True)

        pass

    def parse(self, response):

        # debug页return
        if response.xpath("//div[@class='info']").extract_first() is not None:
            return

        # 拿到yiji
        test_yiji = response.xpath("//ul[@id='con_one_1']/li[contains(@class, 'open')]").extract_first()
        if test_yiji is None:
            yiji = deal_erji_raw_str(response.xpath("//div[@class='shiti_container']/div[2]/h2/b/text()").extract_first())
        else:
            yiji = response.xpath("//ul[@id='con_one_1']/li[contains(@class, 'open')]/a/text()").extract_first()

        # 拿到全页的url
        item_part_urls = response.xpath("//a[@class='view_all']/@href").extract()
        item_urls = []

        # 整理url
        for item in item_part_urls:
            item = "http://" + response.url.split('/')[-2] + "/" + item
            item_urls.append(item)
            pass

        # 遍历全页url进入 详情
        for i in item_urls:
            yield scrapy.Request(url=i,
                                 callback=self.parse_item,
                                 meta={"erji": deal_erji_raw_str(response.xpath("//div[@class='shiti_container']/div[2]/h2/b/text()").extract_first()),
                                       "yiji": yiji},
                                 dont_filter=True)

        # 拿到last_page
        last_page = response.xpath("//div[@class='fenye']/div/a[@class='last']/text()").extract_first()

        # 根据last_page的情况判断是否还有剩余页
        if last_page is None:
            return
        else:
            next_u = response.xpath("//a[@class='nxt']/@href").extract_first()
            yield scrapy.Request(url="http://tiku.21cnjy.com" + next_u, callback=self.parse, dont_filter=True)
            pass
        pass

    def parse_item(self, response):
        loader = ItemLoader(item=MathItem(), response=response)
        loader.add_value('yiji', response.meta["yiji"])
        loader.add_value('erji', response.meta["erji"])

        temp_content = response.text.split("dt>")[-2][:-2]
        loader.add_value('content', temp_content)

        loader.add_value('answer',
                         response.xpath("//div[@class='answer_detail']/dl/dd/p[1]/i/text()").extract_first())

        loader.add_value('analysis',
                         response.xpath("//div[@class='answer_detail']/dl/dd/p[2]/i/text()").extract_first())
        yield loader.load_item()
        pass
