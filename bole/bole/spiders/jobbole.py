# -*- coding: utf-8 -*-
import scrapy
import requests
from bole.items import BoleItem

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['jobbole.com']

    def start_requests(self):
        urls = [
            'http://blog.jobbole.com/114633/',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.css("div.entry-header h1::text").extract_first()
        item = BoleItem(name=title, url=response._url)
        yield item
        for a in response.css("li span.digg-item-updated-title a"):
            href = a.attrib.get("href", None)
            if href:
                yield scrapy.Request(url=href, callback=self.parse)




