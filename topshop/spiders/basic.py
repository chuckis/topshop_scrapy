# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['www.topshop.com']
    start_urls = ['https://www.topshop.com//']

    def parse(self, response):
        urls = response.css('ul.MegaNav-categories > li > a::attr(href)').extract()

        for url in urls:
            yield response.follow(url, callback=self.parse_categories)

    def parse_categories(self, response):
        urls = response.css('nav.MegaNav-subNav > a::attr(href)').extract()

        for url in urls:
            yield response.follow(url, callback=self.parse_product_list)

    def parse_product_list(self, response):
        # products = response.css('div.ProductList-products > div > a::attr(href)').extract()

        self.logger.info("Visited %s", response.url)

        # for product in products:
        #     yield response.follow(product, callback=self.parse_product_detail)

    # def parse_product_detail(self, response):
    #     product_name = response.css('h1.ProductDetail-title ::text').get()
    #     print (product_name)
