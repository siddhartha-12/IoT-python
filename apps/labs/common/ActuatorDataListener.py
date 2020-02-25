'''
Created on Feb 21, 2020

@author: Siddhartha
'''
from labs.module05.MultiActuatorAdaptor import MultiActuatorAdaptor
from labs.common.ActuatorData import ActuatorData
import logging

class ActuatorDataListener:
    def onActuatorMessage(self,ActuatorData):
        #logging.info("Adaptor data -> ")
        #logging.info(ActuatorData)
        MultiActuatorAdaptor.updateActuator(ActuatorData)
        return True
        
        