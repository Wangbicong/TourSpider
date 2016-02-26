# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class TourspiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    item_name = Field()
    url = Field()
    start_place = Field()
    end_place = Field()
    price = Field()
    start_date = Field()
    duration = Field()
    tour_route = Field()
    # hotel = Field()
