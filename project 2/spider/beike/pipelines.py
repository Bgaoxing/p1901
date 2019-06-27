# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from pymongo import MongoClient

client = MongoClient(host='127.0.0.1', port=27017)
db = client.runoob
collection = db.test4


class BeikePipeline(object):
    def process_item(self, item, spider):
        collection.insert(dict(item))
        return item
