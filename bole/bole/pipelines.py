# 数据处理
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo

class BolePipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="12345678",
            charset="utf8mb4",
            database="bole"
        )

    def process_item(self, item, spider):
        cursor = self.conn.cursor()
        sql = 'insert into article (`title`,`url`)values("{}","{}")'.\
            format(item._values.get("name", ""), item._values.get("url", ""))
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()
        return item
