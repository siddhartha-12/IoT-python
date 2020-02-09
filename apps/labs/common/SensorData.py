'''
Created on Jan 30, 2020

@author: Siddhartha
'''
import random
from _datetime import datetime

class SensorData :

    def __init__(self):
        self.current = 0
        self.max_value = 0
        self.min_value = 0
        self.readings_number = 0
        self.sensor_name = "Temperature"
        self.total_value = 0
        self.timestamp = str(datetime.now())
        #self.getCurrentValue()
    
    #Adding current value to the total value and updating other parameters    
    def addValue(self,current):
        self.current = current
        self.timestamp = str(datetime.now());
        self.readings_number += 1
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
            
    #Getter to fetch average 
    def getAverageValue(self):
        return(self.total_value / self.readings_number)
    
    #Getter to count   
    def getCount(self):
        return(self.readings_number)
    
    #Getter to current value
    def getCurrentValue(self):
        return self.current
        
    
    #Getter to fetch max   
    def getMaxValue(self):
        return(self.max_value)
    
    #Getter to fetch min
    def getMinValue(self):
        return(self.min_value)
    #Getter to fetch name of sensor    
    def getName(self):
        return(self.sensor_name)
    #Setter to set name of the sensors
    def setName(self,sname):    
        self.sensor_name = sname     