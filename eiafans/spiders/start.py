# -*- coding: utf-8 -*-
import scrapy
from eiafans.items import EiafansItem
from scrapy.loader import ItemLoader
import socket
import datetime

class StartSpider(scrapy.Spider):
    name = 'start'
    allowed_domains = ['www.eiafans.com']
    start_urls = ['http://www.eiafans.com/']

    def parse(self, response):
        """	This	function	parses	a	property	page.
        @url	http://www.eiafans.com/
        @returns	items	1
        @scrapes	title	price	description	address	image_URL
        @scrapes	url	project	spider	server	date
        """
        # self.log(response.xpath('/html').extract())
        # items = EiafansItem()
        # items['title'] = response.xpath('/html').extract()
        l = ItemLoader(item=EiafansItem(), response=response)
        l.add_xpath('title', '/html')

        l.add_value('url',response.url)
        l.add_value('project',self.settings.get('BOT_NAME'))
        l.add_value('spider',self.name)
        l.add_value('server',socket.gethostname())
        l.add_value('date',datetime.datetime.now())

        return l.load_item()
        pass
