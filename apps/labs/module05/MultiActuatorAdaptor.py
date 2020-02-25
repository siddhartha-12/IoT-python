# +updateActuator(ActuatorData) : boolean. The first and only parameter represents the ActuatorData instance. Returns
# true on successful actuation; false otherwise.
from labs.common.ActuatorData import ActuatorData
from labs.module05.SenseHatLedActivator import SenseHatLedActivator 
from labs.common import ActuatorDataListener
from builtins import staticmethod
import logging
from labs.module05 import PersistenceUtil

#Provide output to senseHat
class MultiActuatorAdaptor:
    #Default Constructor
    __instance = None
    #Implementing Singleton
    @staticmethod
    def getInstance():
        if MultiActuatorAdaptor.__instance == None:
            MultiActuatorAdaptor()
        return MultiActuatorAdaptor.__instance
    
    def __init__(self):
        MultiActuatorAdaptor.__instance = self
    
    def runListener(self):
        adl = ActuatorDataListener.ActuatorDataListener()
        pu = PersistenceUtil.PersistenceUtil()
        logging.info("Starting App \ nPersistenceUtil Created and Registered ")
        pu.registerActuatorDataDbmsListener(adl)
                  
        
    #Updating the actuator data and generating the message body for the led matrix
    @staticmethod
    def updateActuator(ActuatorData):
        hat = SenseHatLedActivator() 
        message ="Current = " + str(ActuatorData.getValue()) + " " +str(ActuatorData.getCommand()) +" <3"
        hat.updateLed(message)
        return True

    