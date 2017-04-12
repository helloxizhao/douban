# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubantestItem(scrapy.Item):
    name = scrapy.Field()
    describe = scrapy.Field()
    director_and_player = scrapy.Field()
