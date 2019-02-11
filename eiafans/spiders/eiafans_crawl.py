# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class EiafansCrawlSpider(CrawlSpider):
    name = 'eiafans_crawl'
    allowed_domains = ['web']
    start_urls = ['http://www.eiafans.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )
    # rules	=	(
    # Rule(LinkExtractor(restrict_xpaths='//*[contains(@class,"next")]')),
    # Rule(LinkExtractor(restrict_xpaths='//*[@itemprop="url"]'),callback='parse_item')
    # )
    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
