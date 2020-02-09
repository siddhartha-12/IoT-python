'''
Created on Jan 30, 2020

@author: Siddhartha
'''
from sense_hat import SenseHat
from _datetime import datetime


class ActuatorData :

    def __init__(self):
        self.max_value = 0
        self.min_value = 0
        self.readings_number = 0
        self.total_value = 0
        self.timestamp = str(datetime.now())
        self.command = "All good"
        self.value = 0.0
        self.name = ""
        self.avgTemp = 0.0
        
    def getAverageValue(self):
        return(self.total_value / self.readings_number)
    
    def getCommand(self): #Returns String commands example Increase Temp
        return self.command
       
    def getValue(self): #Returns the current value
        return self.value    

    def getName(self): # Returns the name of the sensor as a String
        return self.name
    
    def setName(self,name):
        self.name = name
    
    def setCommand(self,command):
        self.command = command
    
    def addValue(self,current):
        self.value = current
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
        
    
       
               