from sense_hat import SenseHat
from labs.common.SensorData import SensorData
from labs.module03 import SensorDataManager
#Call back to SensorDataManager
import threading
from time import sleep


class TempSensorAdaptorTask:
       
    
    def run(self):
        i=0
        while(i<11):
            self.readSensorValue()
            sleep(10)
            i+=1
            
    #Default Constructor    
    def __init__(self):
        self.sensor = SenseHat()
        self.sensorData = SensorData()
        
    #Method for fetching the sensor value from senseHat module   
    def readSensorValue(self):
        temp = self.sensor.get_temperature()
        self.sensorData.addValue(temp)
        self.sdm = SensorDataManager.SensorDataManager()
        self.sdm.hadleSensorData(self.sensorData)
        return self.sensorData.current
        
    