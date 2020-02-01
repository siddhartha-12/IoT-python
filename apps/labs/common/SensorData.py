'''
Created on Jan 30, 2020

@author: Siddhartha
'''
import random
from _datetime import datetime

class SensorData :

    def __init__(self):
        self.max_value = 0
        self.min_value = 0
        self.readings_number =0
        self.sensor_name = "Temperature"
        self.total_value = 0
        self.timestamp = str(datetime.now())
        #self.getCurrentValue()
        
    def addValue(self,current):
        self.timestamp = str(datetime.now());
        if(self.total_value != 0):
            self.total_value += current
            
            if(self.getMaxValue()<current):
                self.max_value = current
            if(self.getMinValue()>current):
                self.min_value = current
            #self.readings_number += 1
        else:
            self.total_value = current
            self.max_value = current
            self.min_value = current
            #self.readings_number = 1
            
      
    def getAverageValue(self):
        return(self.total_value / self.readings_number)
        
    def getCount(self):
        return(self.readings_number)
    
    def getCurrentValue(self):
        current = random.randrange(0,30)
        self.readings_number += 1
        self.addValue(current)
        return current
        
    def getMaxValue(self):
        return(self.max_value)
    
    def getMinValue(self):
        return(self.min_value)
        
    def getName(self):
        return(self.sensor_name)
    
    def setName(self,sname):    
        self.sensor_name = sname     