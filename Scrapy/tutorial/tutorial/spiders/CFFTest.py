# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 12:12:52 2017

@author: reety
"""

import scrapy
import re
from items import CffItem

class CffSpider(scrapy.Spider):

    name = "cffspider"
    start_urls = [ "http://ecocrop.fao.org/ecocrop/srv/en/cropListDetails?code=&relation=beginsWith&name=&quantity="]
    custom_settings = {
    # specifies exported fields and order
    'FEED_EXPORT_FIELDS': ["CropID","SciName", "LifeForm", "Category", "EcocropPhys", "EcocropHabit", "LifeSpan", "PlantAttributes", "SoilDepthOptimal", "SoilDepthAbsolute", "TemperatureOptimalMin", "TemperatureOptimalMax", "TemperatureAbsoluteMin", "TemperatureAbsoluteMax", "SoilTextureOptimal", "SoilTextureAbsolute", "RainOptimalMin", "RainOptimalMax", "RainAbsoluteMin", "RainAbsoluteMax", "SoilFertilityOptimal", "SoilFertilityAbsolute", "LatitudeOptimalMin", "LatitudeOptimalMax", "LatitudeAbsoluteMin", "LatitudeAbsoluteMax", "SoilToxicityOptimal", "SoilToxicityAbsolute", "AltitudeOptimalMin", "AltitudeOptimalMax", "AltitudeAbsoluteMin", "AltitudeAbsoluteMax", "SoilSalinityOptimal", "SoilSalinityAbsolute", "SoilPHOptimalMin", "SoilPHOptimalMax", "SoilPHAbsoluteMin", "SoilPHAbsoluteMax", "SoilDrainageOptimal", "SoilDrainageAbsolute", "LightIntensityOptimalMin", "LightIntensityOptimalMax", "LightIntensityAbsoluteMin", "LightIntensityAbsoluteMax", "ClimateZone", "Photoperiod", "KillingTempRest", "KillingTempEarlyGrowth", "AbioticToler", "AbioticSuscept", "IntroductionRisks", "ProductSystem", "CropCycleMin", "CropCycleMax"],
     }
    
    def parse(self, response):      
  
           for list in response.css('.serviceLink'):
                 link = list.css('::attr(onclick)')
                 id = re.findall(r'\d+', link.extract()[0])[0]
                                                 
                 yield response.follow("http://ecocrop.fao.org/ecocrop/srv/en/dataSheet?id=" + id, self.parse_data)
            
    def parse_data(self, response):
        
            item = CffItem() 
            
            DataLink = response.css('.switchView').css('::attr(href)').extract()[0]
            DataLink = re.findall(r'\d+', DataLink)[0]
            item['CropID'] =  DataLink          
            item['SciName'] = response.xpath('//div[@id="content"]/h2/text()').extract_first()
            item['LifeForm'] = response.xpath('//div[@id="content"]/table[1]/tr[2]/td[1]/text()').extract_first()
            item['Category'] = response.xpath('//div[@id="content"]/table[1]/tr[3]/td[2]/text()').extract_first()
            item['EcocropPhys'] = response.xpath('//div[@id="content"]/table[1]/tr[2]/td[2]/text()').extract_first()
            item['EcocropHabit'] = response.xpath('//div[@id="content"]/table[1]/tr[3]/td[1]/text()').extract_first()
            item['LifeSpan'] = response.xpath('//div[@id="content"]/table[1]/tr[4]/td[1]/text()').extract_first()
            item['PlantAttributes'] = response.xpath('//div[@id="content"]/table[1]/tr[4]/td[2]/text()').extract_first()            
            item['SoilDepthOptimal'] = response.xpath('//div[@id="content"]/table[2]/tr[3]/td[6]/text()').extract_first()
            item['SoilDepthAbsolute'] = response.xpath('//div[@id="content"]/table[2]/tr[3]/td[7]/text()').extract_first()
            
            item['TemperatureOptimalMin'] = response.xpath('//div[@id="content"]/table[2]/tr[4]/td[1]/text()').extract_first()
            item['TemperatureOptimalMax'] = response.xpath('//div[@id="content"]/table[2]/tr[4]/td[2]/text()').extract_first()
            item['TemperatureAbsoluteMin'] = response.xpath('//div[@id="content"]/table[2]/tr[4]/td[3]/text()').extract_first()
            item['TemperatureAbsoluteMax'] = response.xpath('//div[@id="content"]/table[2]/tr[4]/td[4]/text()').extract_first()
            
            item['SoilTextureOptimal'] = response.xpath('//div[@id="content"]/table[2]/tr[4]/td[5]/text()').extract_first()
            item['SoilTextureAbsolute'] = response.xpath('//div[@id="content"]/table[2]/tr[4]/td[6]/text()').extract_first()
            
            item['RainOptimalMin'] = response.xpath('//div[@id="content"]/table[2]/tr[5]/td[1]/text()').extract_first()
            item['RainOptimalMax'] = response.xpath('//div[@id="content"]/table[2]/tr[5]/td[2]/text()').extract_first()
            item['RainAbsoluteMin'] = response.xpath('//div[@id="content"]/table[2]/tr[5]/td[3]/text()').extract_first()
            item['RainAbsoluteMax'] = response.xpath('//div[@id="content"]/table[2]/tr[5]/td[4]/text()').extract_first()
            
            item['SoilFertilityOptimal'] = response.xpath('//div[@id="content"]/table[2]/tr[5]/td[5]/text()').extract_first()
            item['SoilFertilityAbsolute'] = response.xpath('//div[@id="content"]/table[2]/tr[5]/td[6]/text()').extract_first()
            
            item['LatitudeOptimalMin'] = response.xpath('//div[@id="content"]/table[2]/tr[6]/td[1]/text()').extract_first()            
            item['LatitudeOptimalMax'] = response.xpath('//div[@id="content"]/table[2]/tr[6]/td[2]/text()').extract_first()            
            item['LatitudeAbsoluteMin'] = response.xpath('//div[@id="content"]/table[2]/tr[6]/td[3]/text()').extract_first()
            item['LatitudeAbsoluteMax'] = response.xpath('//div[@id="content"]/table[2]/tr[6]/td[4]/text()').extract_first()
            
            item['SoilToxicityOptimal'] = response.xpath('//div[@id="content"]/table[2]/tr[6]/td[5]/text()').extract_first()
            item['SoilToxicityAbsolute'] = response.xpath('//div[@id="content"]/table[2]/tr[6]/td[6]/text()').extract_first()
            
            item['AltitudeOptimalMin'] = response.xpath('//div[@id="content"]/table[2]/tr[7]/td[1]/text()').extract_first()
            item['AltitudeOptimalMax'] = response.xpath('//div[@id="content"]/table[2]/tr[7]/td[2]/text()').extract_first()
            item['AltitudeAbsoluteMin'] = response.xpath('//div[@id="content"]/table[2]/tr[7]/td[3]/text()').extract_first()
            item['AltitudeAbsoluteMax'] = response.xpath('//div[@id="content"]/table[2]/tr[7]/td[4]/text()').extract_first()
            
            item['SoilSalinityOptimal'] = response.xpath('//div[@id="content"]/table[2]/tr[7]/td[5]/text()').extract_first()
            item['SoilSalinityAbsolute'] = response.xpath('//div[@id="content"]/table[2]/tr[7]/td[6]/text()').extract_first()
            
            item['SoilPHOptimalMin'] = response.xpath('//div[@id="content"]/table[2]//tr[8]/td[1]/text()').extract_first()
            item['SoilPHOptimalMax'] = response.xpath('//div[@id="content"]/table[2]/tr[8]/td[2]/text()').extract_first()
            item['SoilPHAbsoluteMin'] = response.xpath('//div[@id="content"]/table[2]/tr[8]/td[3]/text()').extract_first()
            item['SoilPHAbsoluteMax'] = response.xpath('//div[@id="content"]/table[2]/tr[8]/td[4]/text()').extract_first()
            
            item['SoilDrainageOptimal'] = response.xpath('//div[@id="content"]/table[2]/tr[8]/td[5]/text()').extract_first()
            item['SoilDrainageAbsolute'] = response.xpath('//div[@id="content"]/table[2]/tr[8]/td[6]/text()').extract_first()
            item['LightIntensityOptimalMin'] = response.xpath('//div[@id="content"]/table[2]/tr[9]/td[1]/text()').extract_first()
            item['LightIntensityOptimalMax'] = response.xpath('//div[@id="content"]/table[2]/tr[9]/td[2]/text()').extract_first()
            item['LightIntensityAbsoluteMin'] = response.xpath('//div[@id="content"]/table[2]/tr[9]/td[3]/text()').extract_first()
            item['LightIntensityAbsoluteMax'] = response.xpath('//div[@id="content"]/table[2]/tr[9]/td[4]/text()').extract_first()
            item['ClimateZone'] = response.xpath('//div[@id="content"]/table[3]//tr[1]/td[1]/text()').extract_first()
            item['Photoperiod'] = response.xpath('//div[@id="content"]/table[3]/tr[1]/td[2]/text()').extract_first()
            item['KillingTempRest'] = response.xpath('//div[@id="content"]/table[3]/tr[2]/td[1]/text()').extract_first()
            item['KillingTempEarlyGrowth'] = response.xpath('//div[@id="content"]/table[3]/tr[3]/td[1]/text()').extract_first()
            item['AbioticToler'] = response.xpath('//div[@id="content"]/table[3]/tr[3]/td[1]/text()').extract_first()
            item['AbioticSuscept'] = response.xpath('//div[@id="content"]/table[3]/tr[3]/td[2]/text()').extract_first()
            item['IntroductionRisks'] = response.xpath('//div[@id="content"]/table[3]/tr[4]/td[1]/text()').extract_first()
            item['ProductSystem'] = response.xpath('//div[@id="content"]/table[4]/tr[3]/td[1]/text()').extract_first()
            item['CropCycleMin'] = response.xpath('//div[@id="content"]/table[4]/tr[3]/td[2]/text()').extract_first()
            item['CropCycleMax'] = response.xpath('//div[@id="content"]/table[4]/tr[3]/td[3]/text()').extract_first()

            yield item
            
        #tr = response.selector
        #for sel in tr.xpath('//[@id="content"]':
                #item = Field()
               # item['LifeForm']= sel.xpath('//table[1]/tr[2]/td[1]/text()').extract()               
               