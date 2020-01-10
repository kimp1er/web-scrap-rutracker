# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader
from rutracker.items import RutrackerItem


def take_first(loader, item):
    return item[0]


def url_in_first(loader, url):
    link = loader.load_item()['link']
    new_url_is = url[0].urljoin(link)
    return new_url_is


def title_join(loader, title):
    return '|'.join(title)


class RuLoader(ItemLoader):
    title_in = title_join
    title_out = take_first
    link_out = take_first
    url_in = url_in_first
    url_out = take_first
    source_url_out = take_first
    id_out = take_first


class RuTopicLoader(ItemLoader):
    id_out = take_first


class RuspiderSpider(scrapy.Spider):
    name = 'ruspider'
    allowed_domains = ['rutracker.org']
    start_urls = [
        "https://rutracker.org/forum/viewforum.php?f=2221"
    ]

    def parse(self, response):
        topics = response.css('.hl-tr .tt')
        self.logger.info('Topic counts in page is %s' % len(topics))

        for topic in topics:
            yield self.parse_items(topic, response)

    def parse_items(self, selector, response):
        ld = RuLoader(item=RutrackerItem(), selector=selector)
        ld.add_css('title', '.torTopic a ::text')
        ld.add_css('link', '.torTopic a ::attr(href)')
        ld.add_value('url', response)
        ld.add_css('id', '::attr(id)')
        return ld.load_item()
