# -*- coding:utf-8 -*-
# @Author:Liu Guoyang
# @Time  :2019/6/10 12:42
# @File  :draft.py

from pymongo import MongoClient
import csv
import codecs

conn = MongoClient('127.0.0.1', 27017)
db = conn.runoob  # 连接到runoob数据库
my_set = db.test  # 进入test表

cursor = my_set.find()

with codecs.open('data.csv', 'w', 'utf-8') as f:
    writer = csv.writer(f)

    writer.writerow(["name", "type", "district", "address", "area", "price", "total"])

    for data in cursor:
        writer.writerows([[data["name"], data["type"], data["district"], data["address"], data["area"], data["price"], data["total"]]])