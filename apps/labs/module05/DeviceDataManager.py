import logging
from labs.module02.SmtpClientConnector import SmtpClientConnector
from labs.module05.MultiSensorAdaptor import MultiSensorAdaptor
from labs.module05.MultiActuatorAdaptor import MultiActuatorAdaptor
from labs.common.ActuatorData import ActuatorData
from labs.common.SensorData import SensorData
from labs.common.ConfigUtil import ConfigUtil
from labs.module05.PersistenceUtil import PersistenceUtil
from threading import Thread

class DeviceDataManager:
    #Default Constructor
    def __init__(self):
        self.actuator = ActuatorData();
        self.sensorAdaptor = MultiSensorAdaptor()
        self.config = ConfigUtil()
        self.config.loadConfig("../../../config/ConnectedDevicesConfig.props")
        self.threshold = float(self.config.getValue("device", "nominalTemp"))
        self.actuatorOP = MultiActuatorAdaptor.getInstance()

    def run(self):
        t1 = Thread(target=self.sensorAdaptor.getSensorData)
        #logging.info("Running t1")
        t2 = Thread(target=self.actuatorOP.runListener)
        t1.start()
        t2.start()

        
        #self.sensorAdaptor.getSensorData()
    #Method for evaluating the sensor values and create decision for actation  
    def handleActuatorData(self,SensorData):
        self.actuator.max_value = SensorData.max_value
        self.actuator.min_value = SensorData.min_value
        self.actuator.readings_number = SensorData.readings_number
        self.actuator.value  = SensorData.getCurrentValue()
        self.actuator.avgTemp = (SensorData.total_value / SensorData.readings_number)
        self.actuator.total_value = SensorData.total_value
        self.actuator.setName(SensorData.getName())      
        self.actuatorOP.updateActuator(self.actuator)
        #print("Value check - " + str(self.actuator.value))
        #self.sendNotification()
        return True
 
    def handleSensorData(self,SensorData):
        pu = PersistenceUtil()
        pu.writeSensorToDataDbms(SensorData)
        
         