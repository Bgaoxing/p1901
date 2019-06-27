# -*- coding: utf-8 -*-
import scrapy
import bs4



class CeSpider(scrapy.Spider):
    name = 'ce'
    allowed_domains = ['www.ceshi.com']
    start_urls = ['http://10.2.0.193:8000/exercises/spider/level2/']

    def parse(self, response):
        pass


