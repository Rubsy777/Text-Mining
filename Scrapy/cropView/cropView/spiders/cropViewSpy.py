# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 21:21:59 2018

@author: Ruby
"""

 #'text': list.xpath('//div[@id="content"]/table[2]/tr[1]/td')[0].extract()

from __future__ import absolute_import
import scrapy
import re
from cropView.items import CropviewItem

class CropViewSpider(scrapy.Spider):

    name = "cropviewspider"
    start_urls = [ "http://ecocrop.fao.org/ecocrop/srv/en/cropView?id=289"]
    custom_settings = {
    # specifies exported fields and order
    'FEED_EXPORT_FIELDS': ["CropID","SciName", "Info"],
     }
    
    def parse(self, response):      
  
           #for list in response.css('.serviceLink'):
                 #link = list.css('::attr(onclick)')
                 #id = re.findall(r'\d+', link.extract()[0])[0]
                                                 
                 #yield response.follow("http://ecocrop.fao.org/ecocrop/srv/en/cropView?id=" + id, self.parse_data)
            yield response.follow("http://ecocrop.fao.org/ecocrop/srv/en/cropView?id=289", self.parse_data)    
            
    def parse_data(self, response):
        
            item = CropviewItem() 
            
            DataLink = response.css('.switchView').css('::attr(href)').extract()[0]
            DataLink = re.findall(r'\d+', DataLink)[0]
            item['CropID'] =  DataLink          
            item['SciName'] = response.xpath('//div[@id="content"]/h2/text()').extract_first()
            item['Info'] = response.xpath('//div[@id="content"]/table[2]/tr[1]/td/text()')[0].extract()
            yield item