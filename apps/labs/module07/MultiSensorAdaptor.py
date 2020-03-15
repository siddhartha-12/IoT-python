from labs.common.SensorData import SensorData
from labs.module07.HumiditySensorAdaptorTask import HumiditySensorAdaptorTask
from time import sleep
import logging

#Threaded Class
class MultiSensorAdaptor :
    #Default Constructor
    def __init__(self):
        self.sreader = HumiditySensorAdaptorTask() 
        #self.ireader = I2CSensorAdaptorTask()
    #Fetch current readings from the sensor
    def getSensorData(self):
        i = 0
        self.sreader.objectLoader()
        sensorRead = self.sreader.readSensorValue()
        return sensorRead

    