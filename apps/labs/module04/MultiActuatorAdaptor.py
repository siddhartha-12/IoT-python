# +updateActuator(ActuatorData) : boolean. The first and only parameter represents the ActuatorData instance. Returns
# true on successful actuation; false otherwise.
from labs.common.ActuatorData import ActuatorData
from labs.module04.SenseHatLedActivator import SenseHatLedActivator 
from builtins import staticmethod
import logging

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
        self.actuator = ActuatorData()
        self.Humidityi2cdata = ""
        self.HumiditySenseHat = ""
        self.hat = SenseHatLedActivator()       
        
    #Updating the actuator data and generating the message body for the led matrix
    def updateActuator(self,ActuatorData):
        #print("Actuator Name "+ str(ActuatorData.getValue() ))
        if(ActuatorData.getName()=="HumidityI2C"):
            self.Humidityi2cdata = str(ActuatorData.getValue())
        elif(ActuatorData.getName()=="HumiditySenseHat"):
            self.HumiditySenseHat = str(ActuatorData.getValue())
            #print("Actuator Name "+ str(ActuatorData.getValue()))
        message = "Temp -> I2C =" + self.Humidityi2cdata + " SenseHat ="+ self.HumiditySenseHat
        logging.info(message)
        #print("msg : " +message)
        self.hat.updateLed(message)
        return True
    