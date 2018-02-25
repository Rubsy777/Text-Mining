# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:13:49 2018

@author: Ruby
"""
import re
import csv
from quantulum import parser

class ExtractDataCropView(object):
    
    def checkDict(list, dictionary):
        
        paragraph = list[1]
        
        BriefDescription = paragraph.split("USE",1)[0]
        Uses = paragraph.split("USE",1)[1]
        Uses = Uses.split("GROWING PERIOD")[0]
        GrowingPeriod = paragraph.split("GROWING PERIOD",1)[1]
        
        print 'BriefDescription = ' + BriefDescription
        print 'Uses = ' + Uses
        print 'GrowingPeriod = ' + GrowingPeriod
        
        for dictWord in dictionary:
            if re.search(dictWord, Uses, re.IGNORECASE): 
                print 'crop is a food'
                break
            
        if re.search('annual', GrowingPeriod, re.IGNORECASE): 
                print 'crop is Annual'
                
        hpos = BriefDescription.find("height")
        quantsDescription = parser.parse(BriefDescription[hpos-20:hpos+26])
        quantsUses = parser.parse(Uses)
        quantsPeriod = parser.parse(GrowingPeriod)
        print 'BriefDescription Quant:'
        print quantsDescription
        print 'Uses Quant:' 
        print quantsUses
        print 'GrowingPeriod Quant:'
        print quantsPeriod
        #for i in quantsDescription:
        print quantsDescription[0].unit.name # to get the unit's quantity
        print quantsDescription[0].value # to get the amount of the quantity
       
        
            
                
        return;
        
    Food =  ['food', 'cook', 'eat'] 
    
    

    f = open('CropViewCsv.csv')
    
    csv_f = csv.reader(f)
    
    cropID = []
    SciName = []
    Info = []
    
    for row in csv_f:
            cropID.append(row[0])
            SciName.append(row[1])
            Info.append(row[2])
            
    checkDict(Info, Food)
            
        
            
    f.close()
    
    