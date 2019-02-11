# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse
import urllib
from os.path import basename,dirname,join
from eiafans.items import EiafansItem 
from eiafans.tools import get_parameter
from eiafans.tools import dowload_file_path

class EiafansPipeline(object):
    def process_item(self, item, spider):
        return item

class DownloadPipeline(FilesPipeline):

    # def qs(self, url): 
    #     query = urlparse(url).query 
    #     return dict([(k,v[0]) for k,v in urllib.parse.parse_qs(query).items()])

    def file_path(self, request, response=None, info=None):
        path = urlparse(request.url).path
        # print('abc:', get_parameter(request.url)['aid']+'.pdf')
        # item = EiafansItem()
        # print('abc:', item)
        # return item['file_path'][self.qs(request.url)['aid']]+'.pdf' 
        print('abc:', dowload_file_path)
        print('abc:', dowload_file_path[get_parameter(request.url)['aid']])
        e1 = dowload_file_path.pop(get_parameter(request.url)['aid'])
        return dowload_file_path[get_parameter(request.url)['aid']]