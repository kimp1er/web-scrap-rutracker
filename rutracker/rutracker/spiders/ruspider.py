# -*- coding: utf-8 -*-

import scrapy


class RuspiderSpider(scrapy.Spider):
    name = 'ruspider'
    allowed_domains = ['rutracker.org']
    start_urls = [
        "https://rutracker.org/forum/viewforum.php?f=313",
    ]

    def parse(self, response):
        topics = response.css('.hl-tr')
        self.logger.info('Topic counts in page is %s' % len(topics))
        for topic in topics:
            self.logger.info('%s' % topic)
            self.logger.info(topic.__dir__())
            self.logger.info('%s' % topic.css('.tt')[0].get())
            #  self.logger.info('%s' % {
                #  'title': topic.css('vf-col-t-title')[0],
                #  'tor': '',
                #  'replies': '',
                #  'lastpost': ''
            #  })
