from sense_hat import SenseHat
from labs.common.SensorData import SensorData
#from labs.module05 import SensorDataManager
#Call back to SensorDataManager
#import threading
from time import sleep

class HumiditySensorAdaptorTask:
    
    #Default Constructor    
    def __init__(self):
        self.sensor = SenseHat()
        self.sensorData = SensorData()
        self.sdm = None
    #Method to implement lazy object initialization     
    def objectLoader(self):
 
        self.sensorData.setName("HumiditySenseHat")
        #self.sdm = SensorDataManager.SensorDataManager()
            
    #Method for fetching the sensor value from senseHat module   
    def readSensorValue(self):
        humidity = self.sensor.get_humidity()
        self.sensorData.addValue(humidity)
        return self.sensorData
    #Method to push the data to sensorDataManager
        
#     def pushData(self):
#         self.sdm.hadleSensorData(self.sensorData)
#         return True
    
   