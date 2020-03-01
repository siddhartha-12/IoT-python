'''
Created on Feb 21, 2020

@author: Siddhartha
'''
from labs.module05.MultiActuatorAdaptor import MultiActuatorAdaptor

import logging
from labs.common.SensorData import SensorData

class SensorDataListner:
    def onSensorMessage(self,SensorData):
        #logging.info("Adaptor data -> ")
        #logging.info(ActuatorData)
        #MultiActuatorAdaptor.updateActuator(ActuatorData)
        return True
        
        