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
        
        y = 1
        for x in infoList[1:]:
            
            paragraph = x
            
            UsePlant = []
            usesDescription =""        
            Growing = []
            GrowingDescription =""
            
            Uses = None
            GrowingPeriod = None
            BriefDescription = None
            
            elevationDescription0 = None 
            productionDescription0 = None
            productionDescription1 = None 
            heightDescriptio0 = None
            heightDescriptio1 = None
            
            
            heightDescription = None        
            elevationDescription = None        
            productionDescription = None
            
            
            # handle  different patterns of missing parts of paragraph--------------------------------------
            # need to handle if one of the field is missing --------------------------------------------------------
            if ((re.search('description', paragraph, re.IGNORECASE)) and (re.search('use', paragraph, re.IGNORECASE)) and (re.search('GROWING PERIOD', paragraph, re.IGNORECASE))): 
                   BriefDescription = paragraph.split("USE",1)[0]
                   Uses = paragraph.split("USE",1)[1]
                   Uses = Uses.split("GROWING PERIOD")[0]
                   GrowingPeriod = paragraph.split("GROWING PERIOD",1)[1]
            elif ((re.search('description', paragraph, re.IGNORECASE)) and (re.search('GROWING PERIOD', paragraph, re.IGNORECASE))):
                   BriefDescription = paragraph.split("GROWING PERIOD",1)[0]
                   GrowingPeriod = paragraph.split("GROWING PERIOD",1)[1]
            elif ((re.search('description', paragraph, re.IGNORECASE)) and (re.search('use', paragraph, re.IGNORECASE))):
                BriefDescription = paragraph.split("USE",1)[0]
                Uses = paragraph.split("USE",1)[1]
            elif ((re.search('use', paragraph, re.IGNORECASE)) and (re.search('GROWING PERIOD', paragraph, re.IGNORECASE))):
                  Uses = paragraph.split("GROWING PERIOD",1)[0]
                  GrowingPeriod = paragraph.split("GROWING PERIOD",1)[1]
            elif (re.search('description', paragraph, re.IGNORECASE)):
                BriefDescription = paragraph
            elif re.search('use', paragraph, re.IGNORECASE):
                Uses = paragraph
            elif re.search('GROWING PERIOD', paragraph, re.IGNORECASE):
                GrowingPeriod = paragraph
            
            
            
            #print 'BriefDescription = ' + BriefDescription
            #print 'Uses = ' + Uses
            #print 'GrowingPeriod = ' + GrowingPeriod
            
            #USES
            if Uses != None:
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
                    
                #print usesDescription
            
            #GROWING PERIOD
            if GrowingPeriod != None:
                if re.search('annual', GrowingPeriod, re.IGNORECASE): 
                           Growing.append('Annual') 
                            
                if re.search('perennial', GrowingPeriod, re.IGNORECASE): 
                    Growing.append('Perennial')
                            
                if re.search('biennial', GrowingPeriod, re.IGNORECASE): 
                    Growing.append('Biennial')
                    
                #if more than one growing period
                for i in Growing:
                    GrowingDescription = GrowingDescription + '/' +i
                            
                    #print GrowingDescription
                    
                #ELEVATION
                elevationPos = GrowingPeriod.find("elevations")
                elevationDescription = parser.parse(GrowingPeriod[elevationPos-20:elevationPos+26])
                if (len(elevationDescription) == 1):
                    elevationDescription0 = elevationDescription[0].value
                #print 'elevation description'
                #print elevationDescription
                            
                #PRODUCTION
                for dictWord in productionDictionary:
                    if re.search(dictWord, GrowingPeriod, re.IGNORECASE): 
                        productionPos = GrowingPeriod.find(dictWord)
                        productionDescription = parser.parse(GrowingPeriod[productionPos-20:productionPos+26])
                        if (len(productionDescription) == 2):
                            productionDescription0 = productionDescription[0].value
                            productionDescription1 = productionDescription[1].value
                        elif (len(productionDescription) == 1):
                            productionDescription0 = productionDescription[0].value
                            
                        break
                print productionDescription
                  
            
            
                    
            #HEIGHT
            if BriefDescription != None:
                heightPos = BriefDescription.find("height")
                heightDescription = parser.parse(BriefDescription[heightPos-20:heightPos+26])
                if (len(heightDescription) == 2):
                    heightDescriptio0 = heightDescription[0].value
                    heightDescriptio1 = heightDescription[1].value
                elif (len(heightDescription) == 1):
                    heightDescriptio0 = heightDescription[0].value
            
             
            #Exporting data to CSV 
            with open('cropViewData.csv', 'w') as csvfile:
                    fieldnames = ['id', 'Name', 'MinHeight', 'MaxHeight', 'GrowingPeriod', 'Uses', 'Elevation', 'MinProduction', 'MaxProduction']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)   
                    writer.writeheader()                
                    writer.writerow({'id':IDlist[y], 'Name':nameList[y], 'MinHeight':heightDescriptio0, 'MaxHeight':heightDescriptio1, 'GrowingPeriod':GrowingDescription, 'Uses':usesDescription, 'Elevation':elevationDescription0, 'MinProduction':productionDescription0, 'MaxProduction':productionDescription1})
                   
            y = y+1        
            #print heightDescription[0].unit.name # to get the unit's quantity
            #print heightDescription[0].value # to get the amount of the quantity
            #print elevationDescription[0].value # to get the amount of the quantity 
        return;
        
        
        
    Food =  ['food', 'cook', 'eat', 'confection', 'edible', 'beverage', 'drink', 'ferment', 'vege']
    Farming =  ['pasture', 'hay', 'graze', 'poultry', 'pig', 'animal', 'cow', 'livestock', 'fodder', 'cattle', 'sheep', 'crop', 'erosion', 'reforestation']
    Construction =  ['ornament', 'wood', 'construct', 'produce', 'production', 'fiber', 'reclamation', 'timber', 'durable', 'furniture', 'fuel', 'shade', 'industrial', 'tools', 'turnery', 'carving', 'polish', 'terrace', 'shelter']
    Medicinal =  ['Medicinal', 'tonic', 'cure', 'diseases', 'production', 'fiber', 'reclamation']
    Production =["t/ha", "m3/ha"]
       

    f = open('data.csv')
    
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
    
    