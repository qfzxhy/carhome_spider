# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class CardomainItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #car_brand = Field()
    #car_subBrand = Field()
    car_series = Field()
    car_rank = Field()
    pass
