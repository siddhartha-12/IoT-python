'''
Created on Jan 30, 2020

@author: Siddhartha
'''
from sense_hat import SenseHat
from _datetime import datetime


class ActuatorData :
    #Default Constructor
    def __init__(self):
        self.name = ""
        self.reading_number = 0
        self.timestamp = str(datetime.now())
        self.value = 0.0
        self.min_value = 0
        self.max_value = 0        
        self.total_value = 0
        self.command = "All good"        
        self.avgTemp = 0.0
    
    def getTimeStamp(self):
        return self.timestamp
    #Getter for reading counts    
    def getCount(self):
        return self.readings_number
    
    #Getter for Minimum value
    def getMivValue(self):
        return self.min_value
    
    #Getter for maximum count
    def getMaxValue(self):
        return self.max_value 
    
    #Getter for average count    
    def getAverageValue(self):
        return(self.total_value / self.readings_number)
    
    #Getter for Command value
    def getCommand(self): #Returns String commands example Increase Temp
        return self.command
    
    #Getter for getting current actuator value   
    def getValue(self): #Returns the current value
        return self.value    

    #Getter for Sensor name
    def getName(self): # Returns the name of the sensor as a String
        return self.name
    #Setter for sensor name
    def setName(self,name):
        self.name = name
    #Setter for command field
    def setCommand(self,command):
        self.command = command
    
    #Method for adding value to the total
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