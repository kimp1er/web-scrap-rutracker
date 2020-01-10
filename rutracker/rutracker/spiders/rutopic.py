# -*- coding: utf-8 -*-
import scrapy
import redis

r = redis.Redis('192.168.64.6')


class RutopicSpider(scrapy.Spider):
    name = 'rutopic'
    allowed_domains = ['rutracker.org']
    start_urls = ['http://rutracker.org/']

    def parse(self, response):
        pass
