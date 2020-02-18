# -*- coding: utf-8 -*-
import scrapy

#urls = response.css('ul.MegaNav-categories > li > a::attr(href)').extract()

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['https://www.topshop.com/']
    start_urls = ['http://https://www.topshop.com//']

    def parse(self, response):
        pass
