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
            t = topic.css('.tt')[0]
            title = t.css('.torTopic .tt-text')[0]
            title_text = title.css('::text').get()
            link = title.attrib['href']

            self.logger.info('%s' % {
                'title': title_text,
                'link': link
            })
