# -*- coding: utf-8 -*-
import scrapy, bs4
from scrapy import Request
from Jobs.items import ZhaoPinItem
from bs4 import Tag

class ZhaopinSpider(scrapy.Spider):

    name = 'zhaopin'
    allowed_domains = ['zhaopin.com']
    start_offset= 0
    page_size = 90
    data_url = 'https://fe-api.zhaopin.com/c/i/sou?start={}pageSize={}&cityId=801&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&_v=0.62632605&x-zp-page-request-id=4cee26484e154b52900453288b9e15c8-1559554196067-567363&x-zp-client-id=72f75862-c8a3-47b1-bbdd-227b62653ae7'

    def start_requests(self):
        new_url = self.data_url.format(self.start_offset, self.page_size)
        yield Request(url=new_url, callback=self.parse)

    def err_callback(self, *args, **kwargs):
        print("************", args, kwargs)

    def parse(self, response):
        import json


        jobs_data = json.loads(response.text)
        if jobs_data['code'] != 200: # code=200请求才能成功
            return

        reply_jobs = jobs_data['data']['results'] # 所有页面
        if not reply_jobs:
            return
        for job in reply_jobs:
            try:
                item = ZhaoPinItem()
                item["experiences"] = job['workingExp']['name']
                item["salary_range"] = job['salary']
                yield item
            except Exception as e:
                print("xxxxxxxxxxxxx", job)

        self.start_offset += len(reply_jobs) # 当前页面
        new_url = self.data_url.format(self.start_offset, self.page_size)
        print("Requesting {}".format(new_url))
        yield Request(url=new_url, callback=self.parse, errback=self.err_callback)




    # start_offset = 0
    # page_size = 90
    # # start_urls = ['https://sou.zhaopin.com/?jl=801&kw=python&kt=3&sf=0&st=0']
    # date_url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize={}&cityId=801&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&=0&_v=0.98136221&x-zp-page-request-id=d818f450ea0145859bb5fbdc1a6835b6-1559184544312-578301&x-zp-client-id=72f75862-c8a3-47b1-bbdd-227b62653ae7'
    #
    # def start_requests(self):
    #     new_url = self.date_url.format(self.start_offset, self.page_size)
    #     yield Request(url=new_url, callback=self.parse)
    #
    # def err_callback(self, *args, **kwargs):
    #     print("************", args, kwargs)
    #
    # def parse(self, response):
    #     import json
    #     import time
    #     time.sleep(0.5)
    #
    #     jobs_date = json.loads(response.text)
    #     if jobs_date['code'] != 200:
    #         return
    #     reply_jobs = jobs_date['data']['results']
    #     if not reply_jobs:
    #         return
    #
    #     for job in reply_jobs:
    #         try:
    #             item = ZhaoPinItem()
    #             item["experiences"] = job['workingExp']['name']
    #             item["salary_range"] = job['salary']
    #             yield item
    #         except Exception as e:
    #             print("xxxxxxxxxxxxx", job)
    #
    #     self.start_offset += len(reply_jobs)
    #     new_url = self.date_url.format(self.start_offset, self.page_size)
    #     print("Requesting {}".format(new_url))
    #     yield Request(url=new_url,
    #                    callback=self.parse,
    #                    errback=self.err_callback)





