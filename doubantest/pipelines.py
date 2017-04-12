# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
class DoubantestPipeline(object):
    def open_spider(self,spider):
        self.file = codecs.open('items.jl','wb',encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.file.write(line)
        return item
    def close_spider(self, spider):
        self.file.close()
class MysqlDoubanPipeline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool
    @classmethod
    def from_settings(cls,settings):
        dbargs = dict(
             host = settings['MYSQL_HOST'],
             db = settings['MYSQL_DBNAME'],
             user = settings['MYSQL_USER'],
            passwd = settings['MYSQL_PASSWD'],
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = True
        )
        dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)
        return cls(dbpool)
    def process_item(self,item,spider):
        res = self.dbpool.runInteraction(self.insert_into_table,item)
        return item
    def insert_into_table(self,conn,item):
        conn.execute('insert into douban values(%s,%s,%s)',
            (item['name'].encode('utf-8'),
            item['describe'].encode('utf-8'),
            item['director_and_player'][0].encode('utf-8').lstrip()
        ))
