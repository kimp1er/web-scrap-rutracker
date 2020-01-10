# -*- coding: utf-8 -*-
import scrapy
import redis
import json
from scrapy.http import Request

from rutracker.items import RutrackerItemTopic
from scrapy.loader import ItemLoader
from rutracker.settings import REDIS_SETTINGS

r = redis.Redis(**REDIS_SETTINGS)


def take_first(loader, item):
    return item[0]


class RuTopicLoader(ItemLoader):
    id_out = take_first
    source_url_out = take_first


class RutopicSpider(scrapy.Spider):
    name = 'rutopic'
    allowed_domains = ['rutracker.org']
    start_urls = [
        json.loads(r.get(x).decode()) for x in r.keys('RutrackerItem_*')
    ]

    def start_requests(self):
        for i in self.start_urls:
            yield Request(i['url'], dont_filter=True, meta=i)

    def parse(self, response):
        body_elements = response.css('.post_wrap')[0].xpath('div/span[1]')[0]
        ld = RuTopicLoader(item=RutrackerItemTopic(), selector=body_elements)
        ld.add_css('description', '::text')
        ld.add_css('image', '.img-right::attr(title)')
        ld.add_value('source_url', response.url)
        ld.add_value('id', response.meta.get('id'))
        ld.add_value('meta', response.meta)

        return ld.load_item()
