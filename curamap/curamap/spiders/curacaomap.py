# -*- coding: utf-8 -*-
import os
import urllib2
import scrapy


class CuracaomapSpider(scrapy.Spider):
    name = "curacaomap"
    allowed_domains = ["curamap.com"]
    start_urls = (
        'http://www.curamap.com/map/',
    )

    def parse(self, response):
        for link in response.css('li a::attr(href)').re(r'TileGroup.*'):
            yield scrapy.Request(str(self.start_urls[0]) + str(link), self.get_tiles)

    def get_tiles(self, response):
        for image in response.css('li a::attr(href)').re(r'.+.jpg'):
            # I know weird but good ! need to fix this to something more nerdy
            if os.path.exists(os.path.join('..','tiles', image)) == False:
                with open(os.path.join('..','tiles', image), 'w+') as f:
                    f.write(urllib2.urlopen(response.urljoin(image)).read())