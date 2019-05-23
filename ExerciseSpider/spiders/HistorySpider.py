# -*- coding: utf-8 -*-
import requests
import scrapy
from lxml import etree
from scrapy.loader import ItemLoader

from ExerciseSpider.items import HistoryItem
from ExerciseSpider.spiders.utils import util
from ExerciseSpider.spiders.utils.util import deal_erji_raw_str


class HistoryspiderSpider(scrapy.Spider):
    name = 'HistorySpider'
    allowed_domains = ['tiku.21cnjy.com/tiku.php']
    start_urls = ['http://tiku.21cnjy.com/tiku.php/']

    def start_requests(self):

        _u = "http://tiku.21cnjy.com/tiku.php?mod=quest&channel=8&xd=3"

        resp = requests.get(url=_u)
        parser = etree.HTML(resp.text)

        urls = parser.xpath("//ul[@id='con_one_1']//a/@href")

        for u in urls:
            u = "http://tiku.21cnjy.com/tiku.php" + u
            yield scrapy.Request(url=u, callback=self.parse_type, dont_filter=True)

        pass

    def parse_type(self, response):
        types_root = response.xpath("//div[contains(@class, 'shiti_top')]/p[2]/a")

        types_text = types_root.xpath("./text()").extract()[1:]
        types_href = types_root.xpath("./@href").extract()[1:]

        for i in range(len(types_text)):
            yield scrapy.Request(url="http://tiku.21cnjy.com/" + types_href[i],
                                 callback=self.parse,
                                 dont_filter=True,
                                 meta={"type": types_text[i]})

        pass

    def parse(self, response):

        # debug页return
        if response.xpath("//div[@class='info']").extract_first() is not None:
            return

        # 拿到题型
        t_type = response.meta["type"]

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

        # 遍历全页url进入详情
        for i in item_urls:
            yield scrapy.Request(url=i,
                                 callback=self.parse_item,
                                 meta={"erji": deal_erji_raw_str(response.xpath("//div[@class='shiti_container']/div[2]/h2/b/text()").extract_first()),
                                       "yiji": yiji,
                                       "type": t_type},
                                 dont_filter=True)

        # 拿到last_page
        last_page = response.xpath("//div[@class='fenye']/div/a[@class='last']/text()").extract_first()

        # 根据last_page的情况判断是否还有剩余页
        if last_page is None:
            return
        else:
            next_u = response.xpath("//a[@class='nxt']/@href").extract_first()
            yield scrapy.Request(url="http://tiku.21cnjy.com" + next_u, callback=self.parse, dont_filter=True, meta={"type": t_type})
            pass
        pass

    def parse_item(self, response):
        loader = ItemLoader(item=HistoryItem(), response=response)
        loader.add_value('type', response.meta["type"])
        loader.add_value('yiji', response.meta["yiji"])
        loader.add_value('erji', response.meta["erji"])

        parser = etree.HTML(response.text)
        root = parser.xpath("//div['answer_detail']/dl/dt")[0]

        if response.meta["type"] == "单选题" or response.meta["type"] == "多选题":

            # 整理选项
            choose = []
            choose_raw = root.xpath(".//td")
            for item in choose_raw:
                choose.append(util.deal_jam(util.from_choose_item_get_content(etree.tostring(item, encoding='utf-8', pretty_print=True).decode('utf-8'))))
                item.getparent().remove(item)

            # root中剔除table选项
            rm_tb_list = root.xpath(".//table")
            for rm_item in rm_tb_list:
                rm_item.getparent().remove(rm_item)
                pass

            # load
            answer_raw = response.xpath("//div[@class='answer_detail']/dl/dd/p[1]/i/text()").extract_first()
            answer_list = [s_item for s_item in answer_raw]
            answer_index_list = list()

            for answer in answer_list:
                if answer == "A" or answer == "a":
                    answer_index_list.append(0)
                elif answer == "B" or answer == "b":
                    answer_index_list.append(1)
                elif answer == "C" or answer == "c":
                    answer_index_list.append(2)
                elif answer == "D" or answer == "d":
                    answer_index_list.append(3)

            loader.add_value('answer_index', answer_index_list)
            loader.add_value('content', util.from_content_get_real_content(etree.tostring(root, encoding='utf-8', pretty_print=True, method='html').decode('utf-8')))
            loader.add_value('choose', choose)
            pass
        else:
            loader.add_value('content', util.from_content_get_real_content(etree.tostring(root, encoding='utf-8', pretty_print=True, method='html').decode('utf-8')))
            loader.add_value('choose', None)
            pass

        loader.add_value('answer',
                         util.replace_i(response.xpath("//div[@class='answer_detail']/dl/dd/p[1]/i").extract_first()))

        loader.add_value('analysis',
                         util.get_full_analysis(
                             util.replace_i(
                                 response.xpath("//div[@class='answer_detail']/dl/dd/p[2]/i").extract_first())))
        yield loader.load_item()
        pass
