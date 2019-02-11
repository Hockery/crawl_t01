# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EiafansItem(scrapy.Item):
    # define the fields for your item here like:

    # auto download file
    file_urls = scrapy.Field() 
    #
    file_path = scrapy.Field()
    # file which auto download [filename, file_url, file_path] 
    file_download = scrapy.Field()
    # file which need coin  [filename,file_url,coin_buy,coin_down]
    file_coin = scrapy.Field()
    









    #HouseKeeping fields
    url = scrapy.Field() 
    project = scrapy.Field() #
    spider = scrapy.Field()
    server = scrapy.Field()
    date = scrapy.Field()
    #Calculated fields
    images = scrapy.Field()
    location = scrapy.Field()
    #Primary fields
    title = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    address = scrapy.Field()
    image_URL = scrapy.Field()
    pass
