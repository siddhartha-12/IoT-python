# +updateActuator(ActuatorData) : boolean. The first and only parameter represents the ActuatorData instance. Returns
# true on successful actuation; false otherwise.
from labs.common.ActuatorData import ActuatorData
from labs.module03.SenseHatLedActivator import SenseHatLedActivator 


#Provide output to senseHat
class TempActuatorAdaptor:
    #Default Constructor
    def __init__(self):
        self.actuator = ActuatorData()
        
    #Updating the actuator data and generating the message body for the led matrix
    def updateActuator(self,ActuatorData):
        hat = SenseHatLedActivator()
        if(ActuatorData.value>20):
            symbol = " /|\\  :\\"
        elif(ActuatorData.value<20):
            symbol = " \\|/  :/"
        elif(ActuatorData.value==20):
            symbol = " -- -- :)"
        message = "Current Temp " + str(ActuatorData.value) + symbol
        hat.updateLed(message)
        return True
    