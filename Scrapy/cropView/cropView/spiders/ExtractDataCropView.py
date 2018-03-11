# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:13:49 2018

@author: Ruby
"""
import re
import csv
from quantulum import parser

class ExtractDataCropView(object):
    
    def checkDict(infoList, foodDictionary, farmDictionary, constructionDictionary, medicinalDictionary, productionDictionary, IDlist, nameList):
        
        paragraph = infoList[1]
        
        UsePlant = []
        usesDescription =""        
        Growing = []
        GrowingDescription =""
        
        heightDescription = None        
        elevationDescription = None        
        productionDescription = None
        
        BriefDescription = paragraph.split("USE",1)[0]
        Uses = paragraph.split("USE",1)[1]
        Uses = Uses.split("GROWING PERIOD")[0]
        GrowingPeriod = paragraph.split("GROWING PERIOD",1)[1]
        
        print 'BriefDescription = ' + BriefDescription
        print 'Uses = ' + Uses
        print 'GrowingPeriod = ' + GrowingPeriod
        
        #USES
        for dictWord in foodDictionary:
            if re.search(dictWord, Uses, re.IGNORECASE): 
                UsePlant.append('Food') 
                break
            
        for dictWord in farmDictionary:
            if re.search(dictWord, Uses, re.IGNORECASE): 
                UsePlant.append('Farming')
                break
            
        for dictWord in constructionDictionary:
            if re.search(dictWord, Uses, re.IGNORECASE): 
                UsePlant.append('Construction')
                break
            
        for dictWord in medicinalDictionary:
            if re.search(dictWord, Uses, re.IGNORECASE): 
                UsePlant.append('Medicinal')
                break            
        
               
               
         #if more than one growing period
        for i in UsePlant:
            usesDescription = usesDescription + '/' +i
                
        print usesDescription
        
        #GROWING PERIOD
        if re.search('annual', GrowingPeriod, re.IGNORECASE): 
               Growing.append('Annual') 
                
        if re.search('perennial', GrowingPeriod, re.IGNORECASE): 
                Growing.append('Perennial')
                
        if re.search('biennial', GrowingPeriod, re.IGNORECASE): 
                 Growing.append('Biennial')
         
        #if more than one growing period
        for i in Growing:
            GrowingDescription = GrowingDescription + '/' +i
                
        print GrowingDescription
        
        
                
        #HEIGHT
        heightPos = BriefDescription.find("height")
        heightDescription = parser.parse(BriefDescription[heightPos-20:heightPos+26])        
                
        #ELEVATION
        elevationPos = GrowingPeriod.find("elevations")
        elevationDescription = parser.parse(GrowingPeriod[elevationPos-20:elevationPos+26])
        print 'elevation description'
        print elevationDescription
                
        #PRODUCTION
        for dictWord in productionDictionary:
            if re.search(dictWord, GrowingPeriod, re.IGNORECASE): 
                productionPos = GrowingPeriod.find(dictWord)
                print productionPos
                productionDescription = parser.parse(GrowingPeriod[productionPos-20:productionPos+26])
                break
        print productionDescription
        
                
        with open('cropViewData.csv', 'w') as csvfile:
                fieldnames = ['id', 'Name', 'MinHeight', 'MaxHeight', 'GrowingPeriod', 'Uses', 'Elevation', 'MinProduction', 'MaxProduction']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)   
                writer.writeheader()                
                writer.writerow({'id':IDlist[1], 'Name':nameList[1], 'MinHeight':heightDescription[0].value, 'MaxHeight':heightDescription[1].value, 'GrowingPeriod':GrowingDescription, 'Uses':usesDescription, 'Elevation':elevationDescription[0].value, 'MinProduction':productionDescription[0].value, 'MaxProduction':productionDescription[1].value})
               
                
        print heightDescription[0].unit.name # to get the unit's quantity
        print heightDescription[0].value # to get the amount of the quantity
        print elevationDescription[0].value # to get the amount of the quantity
       
        
            
                
        return;
        
    Food =  ['food', 'cook', 'eat', 'confection', 'edible', 'beverage', 'drink', 'ferment', 'vege']
    Farming =  ['pasture', 'hay', 'graze', 'poultry', 'pig', 'animal', 'cow', 'livestock', 'fodder', 'cattle', 'sheep', 'crop', 'erosion', 'reforestation']
    Construction =  ['ornament', 'wood', 'construct', 'produce', 'production', 'fiber', 'reclamation', 'timber', 'durable', 'furniture', 'fuel', 'shade', 'industrial', 'tools', 'turnery', 'carving', 'polish', 'terrace', 'shelter']
    Medicinal =  ['Medicinal', 'tonic', 'cure', 'diseases', 'production', 'fiber', 'reclamation']
    Production =["t/ha", "m3/ha"]
       

    f = open('CropViewCsv.csv')
    
    csv_f = csv.reader(f)   
    
    cropID = []
    SciName = []
    Info = []
    
    for row in csv_f:
            cropID.append(row[0])
            SciName.append(row[1])
            Info.append(row[2])
            
    checkDict(Info, Food, Farming, Construction, Medicinal, Production, cropID, SciName)
            
        
            
    f.close()
    
    