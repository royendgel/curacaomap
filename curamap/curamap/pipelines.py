# -*- coding: utf-8 -*-

class CuramapPipeline(object):
    def process_item(self, item, spider):
        print 'item'
        return item
