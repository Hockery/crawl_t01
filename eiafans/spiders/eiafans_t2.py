# -*- coding: utf-8 -*-
import scrapy
from eiafans.items import EiafansItem
from scrapy.loader import ItemLoader
import socket
import datetime
from eiafans.tools import get_parameter
from eiafans.tools import dowload_file_path
from bs4 import BeautifulSoup
import os

class EiafansT2Spider(scrapy.Spider):
    name = 'eiafans_t2'
    allowed_domains = ['www.eiafans.com']
    start_urls = ['http://www.eiafans.com/forum-64-1.html']
    file_tr_path = []

    def parse(self, response):
        item = {}#EiafansItem() #scrapy.Item()
        # l = ItemLoader(item=EiafansItem(), response=response)
        # l.add_xpath('title', '/html')

        url = 'http://www.eiafans.com/forum.php?mod=attachment&aid=NDAwMTc5fDA5OWY4MGNlfDE1NDk4NTE2ODZ8NDY1MjY1fDExOTM3OTI%3D'
        # l.add_value('file_urls',[url])#,'http://www.eiafans.com/forum.php?mod=attachment&aid=NDAwMTgwfGRkYWZjMTE2fDE1NDk4NTE2ODZ8NDY1MjY1fDExOTM3OTI%3D'])
        # l.add_value('url',response.url)
        # l.add_value('project',self.settings.get('BOT_NAME'))
        # l.add_value('spider',self.name)
        # l.add_value('server',socket.gethostname())
        # l.add_value('date',datetime.datetime.now())
        # print('ccc:', item)
        item['file_urls']=[url]
        item['url']=response.url
        item['project']=self.settings.get('BOT_NAME')
        item['spider']=self.name
        item['server']=socket.gethostname()
        item['date']=datetime.datetime.now()
        item['file_path']={}
        contents = response.xpath('//table/tbody').extract()
        # print(c_id)

        for con in contents:
            try:
                site = BeautifulSoup(con, "html.parser")
            except Exception as e:
                print(e)
            c_id = site.tbody.get("id")
            if c_id is not None and len(c_id) > len('normalthread') and c_id[:len('normalthread')] == 'normalthread':
                print(c_id)
                s_url = os.path.join('http://www.eiafans.com',site.select('th > a[onclick="atarget(this)"]')[0].get('href'))
                print(s_url) # xst"]')[0].get('href'))
                yield scrapy.Request(url=s_url, meta={'loader':item}, callback=self.parse_url, dont_filter=True)
            # print(con)
            # print('______*_____')
            # print(site)
            # a = site.find('tbody').tr.th.a.get('href')
            # print('ccc:', a)
            # yield scrapy.Request(url=a, meta={'loader':l}, callback=self.parse_url, dont_filter=True)
        # xpath_content
        file_id = get_parameter(url)['aid']
        # print('ccc:', file_id)
        dowload_file_path[file_id] = 'abc.pdf' 

        # return  item #l.load_item()
        # pass

    def parse_url(self,response):
        l = response.meta['loader']

        yield l