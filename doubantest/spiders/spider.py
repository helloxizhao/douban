#!/usr/bin/env python
#coding=utf-8
import  scrapy
from  doubantest.items import  DoubantestItem
class doubantest(scrapy.Spider):
    name =  'doubantest'
    start_urls = []
    for i in range(0,100,25):
        url = 'https://movie.douban.com/top250?start=%s&filter='%str(i)
        start_urls.append(url)
    def parse(self, response):
        list = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]')
        for line in list:
            item = DoubantestItem()
            item['name'] = line.xpath('div[1]/a/span[1]/text()').extract()[0]
            item['director_and_player'] = line.xpath('div[2]/p[1]/text()').extract()
            item['describe'] = line.xpath('div[2]/p[2]/span/text()').extract_first()
        #    print item['describe']
            yield item
