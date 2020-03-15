import logging

from labs.module07.MultiSensorAdaptor import MultiSensorAdaptor
from labs.common.SensorData import SensorData
from threading import Thread
from labs.module07.CoapClientConnector import CoapClientConnector
import logging
from time import sleep
from labs.common.DataUtil import DataUtil

class DeviceDataManager:
    #Default Constructor
    def __init__(self):
        self.sensorAdaptor = MultiSensorAdaptor()
        self.ccc = CoapClientConnector()
        
    # Method execution block
    def run(self):
        i=0
        logging.info("Connecting to Server")  
        while(i<1):
            logging.info("Publishing data")
            message = DataUtil.toJsonFromSensorData(self.sensorAdaptor.getSensorData())
            self.ccc.send(message)
            i+=1
            sleep(5)
        logging.info("Finished Publishing")
        return True
    
