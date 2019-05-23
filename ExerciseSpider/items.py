# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ExerciseSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()

    yiji = scrapy.Field()

    erji = scrapy.Field()

    content = scrapy.Field()

    # 选项
    choose = scrapy.Field()

    answer = scrapy.Field()

    answer_index = scrapy.Field()

    analysis = scrapy.Field()
    pass


class EnglishItem(ExerciseSpiderItem):

    pass


class ChineseItem(ExerciseSpiderItem):

    pass


class MathItem(ExerciseSpiderItem):

    pass


class PhysicsItem(ExerciseSpiderItem):

    pass


class ChemistryItem(ExerciseSpiderItem):

    pass


class BiologyItem(ExerciseSpiderItem):

    pass


class GeographyItem(ExerciseSpiderItem):

    pass


class HistoryItem(ExerciseSpiderItem):

    pass


class PoliticsItem(ExerciseSpiderItem):

    pass
