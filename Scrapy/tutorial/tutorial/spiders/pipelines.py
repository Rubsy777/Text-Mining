# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class TutorialPipeline(object):
       

    def process_item(self, item, spider):
        
        item['CropID'] = self.__to_int(item['CropID'])   
        
        item['TemperatureOptimalMin'] = self.__to_int(item['TemperatureOptimalMin'])        
        item['TemperatureOptimalMax'] = self.__to_int(item['TemperatureOptimalMax'])
        item['TemperatureAbsoluteMin'] = self.__to_int(item['TemperatureAbsoluteMin'])        
        item['TemperatureAbsoluteMax'] = self.__to_int(item['TemperatureAbsoluteMax'])
        
        item['RainOptimalMin'] = self.__to_int(item['RainOptimalMin'])        
        item['RainOptimalMax'] = self.__to_int(item['RainOptimalMax'])
        item['RainAbsoluteMin'] = self.__to_int(item['RainAbsoluteMin'])        
        item['RainAbsoluteMax'] = self.__to_int(item['RainAbsoluteMax'])
        
        item['LatitudeOptimalMin'] = self.__to_int(item['LatitudeOptimalMin'])        
        item['LatitudeOptimalMax'] = self.__to_int(item['LatitudeOptimalMax'])
        item['LatitudeAbsoluteMin'] = self.__to_int(item['LatitudeAbsoluteMin'])        
        item['LatitudeAbsoluteMax'] = self.__to_int(item['LatitudeAbsoluteMax'])
        
        item['AltitudeOptimalMin'] = self.__to_int(item['AltitudeOptimalMin'])        
        item['AltitudeOptimalMax'] = self.__to_int(item['AltitudeOptimalMax'])
        item['AltitudeAbsoluteMin'] = self.__to_int(item['AltitudeAbsoluteMin'])        
        item['AltitudeAbsoluteMax'] = self.__to_int(item['AltitudeAbsoluteMax'])
        
        item['SoilPHOptimalMin'] = self.__to_float(item['SoilPHOptimalMin'])        
        item['SoilPHOptimalMax'] = self.__to_float(item['SoilPHOptimalMax'])
        item['SoilPHAbsoluteMin'] = self.__to_float(item['SoilPHAbsoluteMin'])        
        item['SoilPHAbsoluteMax'] = self.__to_float(item['SoilPHAbsoluteMax'])
        
        
                
        return item

    def __to_int(self,value):
		'''
		Convert value to integer type
		'''

		try:
			value = int(value)
		except ValueError:
			value = None

		return value
    
    def __to_float(self,value):
		'''
		Convert value to float type
		'''

		try:
			value = float(value)
		except ValueError:
			value = None

		return value
        