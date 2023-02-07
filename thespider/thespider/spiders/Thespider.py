# -*- coding: utf-8 -*-
from select import select
from __future__ import unicode_literals

import scrapy


class ThespiderSpider(scrapy.Spider):
    name = 'Thespider'
    start_urls = ['https://www.nowinstock.net/videogaming/consoles/sonyps5/']

    def parse(self, response):
        data={}
        stores = response.css('table')
        for store in stores :
            yield {
                'Product_Name' : store.css('a *::text').getall()[0],
                'Stock_Status' : store.css('td.stockStatus *::text').getall()[0]
            }
            



