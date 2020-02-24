from labs.common.SensorData import SensorData
from labs.module05.HumiditySensorAdaptorTask import HumiditySensorAdaptorTask
from labs.module05.PersistenceUtil import PersistenceUtil
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
        putil =PersistenceUtil()
        while(i<1):
            sensorRead = self.sreader.readSensorValue()
            #logging.info("Sending data to putil")
            putil.writeSensorToDataDbms(sensorRead)          
            #self.sreader.pushData()
            i+=1
            sleep(15)
        return True

    