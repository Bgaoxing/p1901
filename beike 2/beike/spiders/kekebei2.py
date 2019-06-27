import scrapy
from scrapy import Request
from bs4 import Tag
from pymongo import MongoClient
from beike.items import BeikeItem
import bs4
import re
import time


class BeikekeSpider(scrapy.Spider):
    name = 'kekebei2'
    start_pgs = ['xinjin', 'jinjiang', 'qingyang', 'jinniu', 'wuhou', 'chenghua', 'longquanyi',
                 'qingbaijiang', 'xindou', 'shuangliu', 'qionglai', 'wenjiang', 'jintang', 'pidou', 'dayi',
                 'pujiang', 'gaoxin7', 'tianfuxinqu', 'jianyang', 'gaoxinxi1', 'tianfuxinqunanqu',
                 ]

    y = 1
    x = 0

    allowed_domains = ['ke.com']
    data_url = 'https://cd.fang.ke.com/ershoufang/{}/pg{}/'

    def start_requests(self):
        cookies = {
            'lianjia_uuid': '65e8368e-1d90-4417-a384-b58ec307b43e',
            ' gr_user_id': '3630c4e8-52d5-49ed-9af1-f0b5e12ad8d3',
            '_ga': 'GA1.2.182941447.1559550961',
            'ke_uuid': 'b7f11f687d914a5b48df9fbf24436eb1',
        }
        parse_url = self.data_url.format(self.start_pgs[self.x], self.y)
        yield Request(url=parse_url, cookies=cookies, meta={'dont_redirect': True, 'handle_httpstatus_list': [302]},
                      callback=self.parse)

    def err_callback(self, *args, **kwargs):
        print('*******', args, kwargs)

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text)
        # numbers = bs.find('div',attrs={'class':'page-box house-lst-page-box'})
        # number = response.css('.page-box house-lst-page-box div::attr(page-data)').extract()
        number = response.xpath('//div[@class="page-box house-lst-page-box"]/../@page-data')

        # find('div', attrs={'class': 'se-link-container'})
        item = BeikeItem()
        items_div = bs.find_all("div", attrs={"class": "content"})
        # assert isinstance(items_div,Tag)
        t = items_div.find('li', attrs={'class': 'clear'}, recursive=True)
        for item_li in t:
            assert isinstance(item_li, Tag)
            details = item_li.find('div', attrs={'class': 'info clear'})
            name = details.find('a', attrs={'class': "VIEWDATA CLICKDATA maidian-detail"}).text  # 小区名字
            type = details.find('div', attrs={'class': 'resblock-name'}).select('span')[-1].text
            location = details.find("div", attrs={"class": "address"}).text
            address = location.select('a').text
            prices = details.find('div', attrs={'class': 'priceInfo'}).select('span')[-1].text
            price = re.match(r'\d+', prices)
            try:
                area = details.find('div', attrs={'class': 'houseInfo'}).text
                for i in re.findall(r"\d+", area)[-1]:
                    area = i
            except:
                area = 0
            total = details.find('div', attrs={'class': 'priceInfo'}).select('span')[0].text
            print('-------------')
            item['name'] = name
            item['type'] = type

            item['address'] = address
            item['area'] = area
            item['price'] = price
            item['total'] = total

            yield item
        time.sleep(0.6)

        # 开始爬取多页

        self.y += 1
        if self.y <= int(number):  # 可以看到贝壳房-新房，网站上只有100页

            parse_url = self.data_url.format(self.start_pgs[self.x], self.y)
            yield Request(url=parse_url, meta={'dont_redirect': True, 'handle_httpstatus_list': [302]},
                          callback=self.parse, errback=self.err_callback,
                          )

        else:
            self.y = 1
            self.x += 1
            if self.x <= len(self.start_pgs) - 1:
                parse_url = self.data_url.format(self.start_pgs[self.x], self.y)
                yield Request(url=parse_url, meta={'dont_redirect': True, 'handle_httpstatus_list': [302]},
                              callback=self.parse, errback=self.err_callback, dont_filter=True)
            else:
                return


