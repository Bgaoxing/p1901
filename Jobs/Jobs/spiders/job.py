# -*- coding: utf-8 -*-
import scrapy
import bs4
from bs4 import Tag
from scrapy import Request
from Jobs.items import JobsItem

class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['www.51job.com']
    # start_urls = ['http://www.51job.com/']

    def start_requests(self):
        yield Request(url='http://it.51job.com/hotjobs.php#itStar',
                      callback=self.parse)

    def parse_job(self, response):
        import bs4
        bs = bs4.BeautifulSoup(response.text)
        for job in bs.find("div", attrs={"class": "items"}).find_all("a"):
            item = JobsItem()
            item["title"] = job.find("aside").text
            item['city'] = job.find("i").text
            item['salary_range'] = job.find('em').text
            # print(item)
            yield item

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text)
        dj_host_element = bs.find('div', attrs={'class': 'dj_hot'})
        assert isinstance(dj_host_element, Tag)
        for job in dj_host_element.find_all('div', attrs={'class': 'e'}, recursive=True):
            assert isinstance(job, Tag)
            item = JobsItem()
            item['title'] = job.find('p', attrs={'class': 'jname'}).find('a').text
            item['salary_range'] = job.find('span', attrs={'class': 'sal'}).text
            info = job.find('p', attrs={'class': 'tab'}).find_all('span')
            if len(info) >= 4:
                item['city'] = info[0].text
                item["experiences"] = info[1].text
                item['education'] = info[2].text
                item['dist_time'] = info[3].text

            elif len(info) == 2:
                item["city"] = info[0].text
                item['dist_time'] = info[1].text
            elif len(info) == 3:
                item["city"] = info[0].text
                item["experiences"] = info[1].text
                item['dist_time'] = info[2].text
            yield item

        yield Request(
            url="https://m.51job.com/search/joblist.php?keyword=%E4%BA%A7%E5%93%81%E7%AD%96%E5%88%92&keywordtype=2&funtype=0000&indtype=00&jobarea=090200&jobterm=99&cotype=99&issuedate=9&saltype=99&degree=99&landmark=0&workyear=99&cosize=99&radius=-1&lonlat=0%2C0",
            callback=self.parse_job)




