'''
Created on Apr 11, 2020

@author: Siddhartha
'''
class PlantDeviceSensorData():
    def __init__(self):
        self.temperature = 0.0
        self.humidity = 0.0
        self.ldr = 0.0
        self.soilMoisture = 0.0
        self.GatewayMemoryUtil = 0.0
        self.GateCpuUtil = 0.0
        self.ConstrainCpuUtil = 0.0
        self.ConstrainMemoryUtil = 0.0
        self.timeStamp = ""
    
    def getTemperature(self):
        return self.temperature;
    

    def setTemperature(self,temperature):
        self.temperature = temperature;
    

    def getHumidity(self):
        return self.humidity;
    

    def setHumidity(self,humidity):
        self.humidity = humidity;
    

    def getLdr(self):
        return self.ldr;
    

    def setLdr(self,ldr):
        self.ldr = ldr;
    

    def getSoilMoisture(self):
        return self.soilMoisture;
    

    def setSoilMoisture(self,soilMoisure):
        self.soilMoisture = soilMoisure;
    

    def getGatewayMemoryUtil(self):
        return self.GatewayMemoryUtil;
    

    def setGatewayMemoryUtil(self,gatewayMemoryUtil):
        self.GatewayMemoryUtil = gatewayMemoryUtil;
    

    def getGateCpuUtil(self):
        return self.GateCpuUtil;
    

    def setGateCpuUtil(self,gateCpuUtil):
        self.GateCpuUtil = gateCpuUtil;
    

    def getConstrainCpuUtil(self):
        return self.ConstrainCpuUtil;
    

    def setConstrainCpuUtil(self,constrainCpuUtil):
        self.ConstrainCpuUtil = constrainCpuUtil;
    
    def getConstrainMemoryUtil(self):
        return self.ConstrainMemoryUtil;
    

    def setConstrainMemoryUtil(self,constrainMemoryUtil):
        self.ConstrainMemoryUtil = constrainMemoryUtil;
    

    def getTimeStamp(self):
        return self.timeStamp;
    

    def setTimeStamp(self,timeStamp):
        self.timeStamp = timeStamp;
    