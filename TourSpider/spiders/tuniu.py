from scrapy import Spider

class TuniuSpider(Spider):
    name = 'tuniu'
    allowed_domains = ['tuniu.com']
    start_urls = [
        'http://s.tuniu.com/search_complex/whole-zz-0-%E5%8F%B0%E6%B9%BE/'
    ]

    def parse(self, response):
        print response.body