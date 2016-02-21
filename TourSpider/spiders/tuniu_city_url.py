# coding:utf-8
from scrapy import Spider
import codecs

class TuniuUrlSpider(Spider):

    name = 'tuniuurl'
    allowed_domains = ['tuniu.com']
    start_urls = [
        'http://s.tuniu.com/search_complex/whole-bj-0-台湾/1/'
    ]

    def parse(self, response):

        for sites in response.xpath('//div[@class="line_right"]'):
            for site in sites.xpath('//a/@href'):
                with codecs.open('TourSpider/data/tuniu_city_url', 'a', 'utf-8') as f:
                    f.write(site.extract()+'\n')

