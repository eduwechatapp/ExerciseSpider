# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EnglishspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class EnglishWordItem(scrapy.Item):

    yiji = scrapy.Field()

    erji = scrapy.Field()

    content = scrapy.Field()

    answer = scrapy.Field()

    analysis = scrapy.Field()

    pass
