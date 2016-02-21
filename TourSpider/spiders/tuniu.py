# coding:utf-8
from scrapy import Spider, Request
from TourSpider.items import TourspiderItem


class TuniuSpider(Spider):
    name = 'tuniu'
    allowed_domains = ['tuniu.com']

    start_urls = []
    with open('TourSpider/data/tuniu_city_url') as city_url_file:
        for city_url in city_url_file:
            start_urls.append(city_url.strip())

    def parse(self, response):

        sites = response.xpath('//div[@class="theinfo clearfix"]')

        for site in sites:
            item = TourspiderItem()

            item['item_name'] = site.xpath('dl[@class="detail"]/dt/p[@class="title"]/a/@title').extract()
            item['start_place'] = site.xpath('dl[@class="detail"]/dt/p[@class="subtitle"]/'
                                             'span[@class="c_green"]/text()').extract()
            item['end_place'] = response.url.split('/')[-3].split('-')[-1]
            item['price'] = site.xpath('div[@class="priceinfo"]/span[@class="tnPrice"]/em/text()').extract()
            item['start_date'] = site.xpath('dl[@class="detail"]/dd[@class="tqs"]/'
                                            'span/a/text()').extract()
            item['duration'] = site.xpath('dl[@class="detail"]/dd[@class="port"]/span/text()').extract()
            item['tour_route'] = site.xpath('dl[@class="detail"]/dd[@class="overview"]/text()').extract()
            yield item

        next_link = response.xpath('//a[@class="page-next"]/@href').extract()
        if next_link:
            yield Request(next_link[0], callback=self.parse)
