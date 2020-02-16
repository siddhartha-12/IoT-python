from sense_hat import SenseHat
from labs.common.SensorData import SensorData
from labs.module04 import SensorDataManager
#Call back to SensorDataManager
#import threading
from time import sleep

from pip._internal import self_outdated_check



class HumiditySensorAdaptorTask:
    
    #Default Constructor    
    def __init__(self):
        self.sensor = SenseHat()
        self.sensorData = None
        self.sdm = None
        
    def objectLoader(self):
        self.sensorData = SensorData()
        self.sensorData.setName("HumiditySenseHat")
        self.sdm = SensorDataManager.SensorDataManager()
            
    #Method for fetching the sensor value from senseHat module   
    def readSensorValue(self):
        humidity = self.sensor.get_humidity()
        self.sensorData.addValue(humidity)
        return self.sensorData.current
    
    def pushData(self):
        self.sdm.hadleSensorData(self.sensorData)
    
   