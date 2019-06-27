import scrapy
from scrapy import Request
from bs4 import Tag
from pymongo import MongoClient
from beike.items import BeikeItem
import bs4
import re
import time

class BeikekeSpider(scrapy.Spider):
    name = 'kekebei'
    start_pgs = ['xinjin','jinjiang','qiangyang','jinniu','wuhou','chenghua','longquanyi',
                'qingbaijiang','xindou','shuangliu','qionglai','wenjiang','jintang','shuangliu','pidou','dayi',
                'pujiang','gaoxin7','tianfuxinqu','jianyang','gaoxinxi1','tianfuxingqunanqu'
                ]

    y = 1
    x = 0

    allowed_domains = ['ke.com']
    data_url = 'https://cd.fang.ke.com/loupan/{}/pg{}/#{}'
    def start_requests(self):

        parse_url = self.data_url.format(self.start_pgs[self.x],self.y,self.start_pgs[self.x])
        yield Request(url=parse_url, callback=self.parse)

    def err_callback(self,*args,**kwargs):
        print('*******',args,kwargs)
    def parse(self, response):

        bs = bs4.BeautifulSoup(response.text)
        numbers = bs.find_all('section',attrs={'class':"se-part"})[-1]
        number = numbers.select('a')[-1].text
        # find('div', attrs={'class': 'se-link-container'})
        item = BeikeItem()
        items_div = bs.find('div', attrs={'class':"resblock-list-container clearfix"})
        assert isinstance(items_div,Tag)
        for item_li in items_div.find_all('li',attrs={'class':'resblock-list post_ulog_exposure_scroll has-results'},recursive=True):
            assert isinstance(item_li,Tag)
            details = item_li.find('div',attrs={'class':'resblock-desc-wrapper'})
            name = details.find('a',attrs= {'class':"name"}).text #小区名字
            type = details.find('div',attrs = {'class':'resblock-name'}).select('span')[-1].text
            location = details.find("a", attrs={"class": "resblock-location"}).text
            district = location.split('/')[0]
            district = district.split('\n')[1] #区域

            address = location.split('/')[-1]
            address = address.split('\n\t\t')[0]  #地址
            try:
                area = details.find('a',attrs={'class':'resblock-room'}).select('span')[-1].text
                area = area.split(' ')[1]
            except:
                area = '待定'
            price = details.find('span',attrs = {'class':'number'}).text
            try:
                total = details.find('div',attrs = {'class':'second'}).text
                for i in re.findall(r"\d+",total):
                    total = i
            except:
                total = 0
            print('-------------')
            item['name'] = name
            item['type'] = type
            item['district'] = district
            item['address'] = address
            item['area'] = area
            item['price'] = price
            item['total'] = total

            yield item
        time.sleep(0.2)

        # 开始爬取多页

        self.y += 1
        if self.y <= int(number):  # 可以看到贝壳房-新房，网站上只有100页

            parse_url = self.data_url.format(self.start_pgs[self.x],self.y,self.start_pgs[self.x])
            yield Request(url=parse_url, callback=self.parse, errback=self.err_callback)



        else:
            self.y = 1
            self.x += 1
            if self.x <= len(self.start_pgs):
                parse_url = self.data_url.format(self.start_pgs[self.x], self.y, self.start_pgs[self.x])
                yield Request(url=parse_url, callback=self.parse, errback=self.err_callback)
            else:
                return