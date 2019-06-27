# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

# class JobsPipeline(object):
#     # def __init__(self):
#     #     self.conn = pymysql.connect(
#     #         host="127.0.0.1",
#     #         user="root",
#     #         password="12345678",
#     #         charset="utf8mb4",
#     #         database="bole"
#     #     )
#
#
#     def process_item(self, item, spider):
#         # cursor = self.conn.cursor()
#         # sql = 'insert into info (`title`,`city`,`experiences`,`education`,`dist_time`,`salary_range`)' \
#         #       'values("{}","{}","{}","{}","{}","{}")'. \
#         #     format(item._values.get("title", ""), item._values.get("city", ""),
#         #            item._values.get("experiences", ""), item._values.get("education", ""),
#         #            item._values.get("dist_time", ""), item._values.get("salary_range", ""))
#         # cursor.execute(sql)
#         # self.conn.commit()
#         # cursor.close()
#         return item

class JobsPipeline(object):
    def open_spider(self, spider):
        self.data_fp = open("./data.csv", "w")
        import csv
        self.csv_writer = csv.DictWriter(self.data_fp, fieldnames=("experiences", "salary_range"))
        self.csv_writer.writeheader()

    def process_item(self, item, spider):
        self.csv_writer.writerow({"experiences": item["experiences"], "salary_range": item["salary_range"]})
        return item

    def close_spider(self, spider):
        self.data_fp.close()