# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import random
import time

import pymongo

import pymysql

from ExerciseSpider.spiders.utils import util


def get_data(item):
    if "yiji" not in item:
        yiji = ""
    else:
        yiji = item["yiji"][0]

    if "erji" not in item:
        erji = ""
    else:
        erji = item["erji"][0]

    if "content" not in item:
        content = ""
    else:
        content = item["content"][0]

    if "answer" not in item:
        answer = ""
    else:
        answer = item["answer"][0]

    if "analysis" not in item:
        analysis = ""
    else:
        analysis = item["analysis"][0]

    if "type" not in item:
        type = ""
    else:
        type = item["type"][0]

    if "choose" not in item:
        choose = []
    else:
        choose = item["choose"]

    if "answer_index" not in item:
        answer_index = []
    else:
        answer_index = item["answer_index"]

    return {
        "_id": util.md5(yiji + erji + type + answer + str(random.randint(0, 255)) + str(round(time.time() * 1000))),
        "yiji": yiji,
        "erji": erji,
        "content": content,
        "answer": answer,
        "type": type,
        "analysis": analysis,
        "choose": choose,
        "answer_index": answer_index
    }
    pass


class EnglishSpiderPipeline(object):

    mongo_uri = "mongodb://127.0.0.1"

    collection_name = "english_lib"

    db_name = "exercise_lib"

    def __init__(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.db_name]

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = get_data(item)
        self.db[self.collection_name].insert_one(data)
        return item


class ChineseSpiderPipeline(object):

    mongo_uri = "mongodb://127.0.0.1"

    collection_name = "chinese_lib"

    db_name = "exercise_lib"

    def __init__(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.db_name]

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = get_data(item)
        self.db[self.collection_name].insert_one(data)
        return item


class MathSpiderPipeline(object):

    mongo_uri = "mongodb://127.0.0.1"

    collection_name = "math_lib"

    db_name = "exercise_lib"

    def __init__(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.db_name]

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = get_data(item)
        self.db[self.collection_name].insert_one(data)
        return item


class PhysicsSpiderPipeline(object):

    mongo_uri = "mongodb://127.0.0.1"

    collection_name = "physics_lib"

    db_name = "exercise_lib"

    def __init__(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.db_name]

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = get_data(item)
        self.db[self.collection_name].insert_one(data)
        return item


class ChemistrySpiderPipeline(object):

    mongo_uri = "mongodb://127.0.0.1"

    collection_name = "chemistry_lib"

    db_name = "exercise_lib"

    def __init__(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.db_name]

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = get_data(item)
        self.db[self.collection_name].insert_one(data)
        return item


class BiologySpiderPipeline(object):

    mongo_uri = "mongodb://127.0.0.1"

    collection_name = "biology_lib"

    db_name = "exercise_lib"

    def __init__(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.db_name]

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = get_data(item)
        self.db[self.collection_name].insert_one(data)
        return item


class GeographySpiderPipeline(object):

    mongo_uri = "mongodb://127.0.0.1"

    collection_name = "geography_lib"

    db_name = "exercise_lib"

    def __init__(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.db_name]

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = get_data(item)
        self.db[self.collection_name].insert_one(data)
        return item


class HistorySpiderPipeline(object):

    mongo_uri = "mongodb://127.0.0.1"

    collection_name = "history_lib"

    db_name = "exercise_lib"

    def __init__(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.db_name]

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = get_data(item)
        self.db[self.collection_name].insert_one(data)
        return item

class PoliticsSpiderPipeline(object):

    mongo_uri = "mongodb://127.0.0.1"

    collection_name = "politics_lib"

    db_name = "exercise_lib"

    def __init__(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.db_name]

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = get_data(item)
        self.db[self.collection_name].insert_one(data)
        return item
