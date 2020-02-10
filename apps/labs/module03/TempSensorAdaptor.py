from labs.common.SensorData import SensorData
from labs.module03.TempSensorAdaptorTask import TempSensorAdaptorTask
import logging
from email.policy import SMTP

#Threaded Class

class TempSensorAdaptor :
    #Default Constructor
    def __init__(self):
        self.sreader = TempSensorAdaptorTask() 
        

    #Fetch current readings from the sensor
    def getSensorData(self):
        self.sreader.run()
        return True

    