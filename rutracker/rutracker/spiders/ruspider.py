# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join
from rutracker.items import RutrackerItem
import logging


def link_out_first(loader, item):
    logging.info(f'Loader is {loader}')
    return item[0]


def url_in_first(loader, url):
    link = loader.load_item()['link']
    new_url_is = url[0].urljoin(link)
    return new_url_is


def url_out_first(loader, url):
    return url[0]


class RuLoader(ItemLoader):
    title_out = Join()
    link_out = link_out_first
    url_in = url_in_first
    url_out = url_out_first


class RuspiderSpider(scrapy.Spider):
    name = 'ruspider'
    allowed_domains = ['rutracker.org']
    start_urls = [
        "https://rutracker.org/forum/viewforum.php?f=194",
    ]

    def parse(self, response):
        topics = response.css('.hl-tr .tt')
        self.logger.info('Topic counts in page is %s' % len(topics))

        for topic in topics:
            yield self.parse_items(topic, response)

    def parse_items(self, selector, response):
        ld = RuLoader(item=RutrackerItem(), selector=selector)
        ld.add_css('title', '.torTopic a ::text', Join())
        ld.add_css('link', '.torTopic a ::attr(href)')
        ld.add_value('url', response)
        return ld.load_item()
