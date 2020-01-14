#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
from scrapy.exporters import BaseItemExporter
from scrapy.utils.serialize import ScrapyJSONEncoder
from scrapy.utils.python import to_bytes


class RedisRutrackerExporter(BaseItemExporter):
    def __init__(self, redis_settings, **kwargs):
        super(BaseItemExporter, self).__init__(**kwargs)
        self._configure(kwargs, dont_fail=True)
        self.encoding = 'UTF-8'
        self.encoder = ScrapyJSONEncoder(**kwargs)
        self.db = redis.Redis(**redis_settings)

    def export_item(self, item):
        itemdict = dict(self._get_serialized_fields(item))
        data = self.encoder.encode(itemdict) + '\n'
        item_id = item.get('id')

        key_prefix = f'{item.__class__.__name__}_{ item_id }'

        self.db.set(
            name=key_prefix,
            value=to_bytes(data, self.encoding),
            ex=1231244
        )
