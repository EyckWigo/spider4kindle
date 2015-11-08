# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

class dailynewsPipeline(object):
    def __init__(self):
        self.file = codecs.open('result.html', mode='wb', encoding = 'utf-8')

    def process_item(self, item, spider):
        dicts = dict(item)
        line = "<html><body><h2>" + str(dicts['title']) + "</h2>"
        line = line + str(dicts['content']) + "</body></html>"
        #line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode('unicode_escape'))
        return item
