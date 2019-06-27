# -*- coding: utf-8 -*-
import scrapy
import bs4
from Jobs.items import XiaoHuaItem
class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['xiaohua.com']
    start_urls = ['http://www.xiaohuar.com/list-1-0.html']

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text)
        item = XiaoHuaItem()
        items_div = bs.find("div", attrs={"class": "item_list infinite_scroll"})
        img_urls = []
        for img in items_div.find_all("div", attrs={
            "class": "item_t"}, recursive=True):
            pic_info = img.find("img")
            img_url = "http://www.xiaohuar.com" + pic_info.attrs["src"]
            img_urls.append(img_url)

        item["image_urls"] = img_urls
        print(item["image_urls"])
        yield item

