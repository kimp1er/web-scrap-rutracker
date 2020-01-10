# -*- coding: utf-8 -*-
import scrapy
import redis
import json

r = redis.Redis('192.168.64.6')


class RutopicSpider(scrapy.Spider):
    name = 'rutopic'
    allowed_domains = ['rutracker.org']
    start_urls = [
        json.loads(r.get(x).decode())['url'] for x in r.keys('rutracker_*')
    ]

    def parse(self, response):
        pass
