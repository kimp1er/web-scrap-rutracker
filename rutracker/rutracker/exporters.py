#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
from scrapy.exporters import BaseItemExporter
from scrapy.utils.serialize import ScrapyJSONEncoder
from scrapy.utils.python import to_bytes


class RedisRutrackerExporter(BaseItemExporter):
    def __init__(self, host, **kwargs):
        self._configure(kwargs, dont_fail=True)
        kwargs.setdefault('ensure_ascii', not self.encoding)
        self.encoder = ScrapyJSONEncoder(**kwargs)
        self.db = redis.Redis(host)

    def export_item(self, item):
        itemdict = dict(self._get_serialized_fields(item))
        data = self.encoder.encode(itemdict) + '\n'
        self.db.set(
            name='rutracker_' + item.get('id'),
            value=to_bytes(data, self.encoding),
            ex=600
        )
