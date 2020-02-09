# +updateActuator(ActuatorData) : boolean. The first and only parameter represents the ActuatorData instance. Returns
# true on successful actuation; false otherwise.
from labs.common.ActuatorData import ActuatorData
from labs.module03.SenseHatLedActivator import SenseHatLedActivator 


#Provide output to senseHat
class TempActuatorAdaptor:

    def __init__(self):
        self.actuator = ActuatorData()
        
    
    def updateActuator(self,Actuator):
        hat = SenseHatLedActivator()
        hat.updateLed(Actuator.getCommand())
        return True
    