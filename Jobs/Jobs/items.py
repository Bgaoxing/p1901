# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    city = scrapy.Field()
    experiences = scrapy.Field() # 经验
    education = scrapy.Field() # 学历
    dist_time = scrapy.Field()
    salary_range = scrapy.Field() # 工资范围

class XiaoHuaItem(scrapy.Item):
    image_urls = scrapy.Field()

class ZhaoPinItem(scrapy.Item):
    salary_range = scrapy.Field()
    experiences = scrapy.Field()







