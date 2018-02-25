# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from __future__ import absolute_import
import scrapy


class CropviewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    CropID = scrapy.Field()    
    SciName = scrapy.Field()
    Info = scrapy.Field()
