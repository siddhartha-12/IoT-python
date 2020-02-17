from labs.common.SensorData import SensorData
import logging
from labs.module04.HumiditySensorAdaptorTask import HumiditySensorAdaptorTask
from labs.module04.I2CSensorAdaptorTask import I2CSensorAdaptorTask
from labs.module04 import SensorDataManager
from time import sleep

#Threaded Class

class MultiSensorAdaptor :
    #Default Constructor
    def __init__(self):
        self.sreader = HumiditySensorAdaptorTask() 
        #self.ireader = I2CSensorAdaptorTask()
        

    #Fetch current readings from the sensor
    def getSensorData(self):
        i = 0
        self.ireader.objectLoader()
        self.sreader.objectLoader()
        while(i<5):
            self.sreader.readSensorValue()
            sleep(0.0001)
            self.ireader.displayHumidityData()
            self.sreader.pushData()
            self.ireader.pushData()
            i+=1
            sleep(5)
        return True

    