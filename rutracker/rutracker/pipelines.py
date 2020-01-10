# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
from rutracker.exporters import RedisRutrackerExporter


class RutrackerPipeline(object):

    def open_spider(self, spider):
        self.exporter = RedisRutrackerExporter('192.168.64.6')
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()

    def process_item(self, item, spider):
        logging.info(f'Pipeline item is: {item}')
        logging.info(f'Pipeline spider is: {spider}')
        self.exporter.export_item(item),
        return item
