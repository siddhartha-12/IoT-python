'''
Created on Jan 30, 2020

@author: Siddhartha
'''
import logging
from labs.module06.MultiSensorAdaptor import MultiSensorAdaptor
from labs.common.SensorData import SensorData
from threading import Thread
from labs.module06.MqttClientConnector import MqttClientConnector
import logging
from time import sleep
from labs.common.DataUtil import DataUtil
class DeviceDataManager:
    #Default Constructor
    def __init__(self):
        self.sensorAdaptor = MultiSensorAdaptor()
        self.mqtt = MqttClientConnector()
        
    # Method execution block
    def run(self):
        i=0
        logging.info("Connecting to broker")
        self.mqtt.connect()
        logging.info("Connecting to broker")    
        while(i<2):
            logging.info("Publishing data using QoS1")
            message = DataUtil.toJsonFromSensorData(self.sensorAdaptor.getSensorData())
            self.mqtt.publishSensorData(message,1)
            i+=1
            sleep(5)
        while(i<4):
            logging.info("Publishing data using QoS2")
            message = DataUtil.toJsonFromSensorData(self.sensorAdaptor.getSensorData())
            self.mqtt.publishSensorData(message,2)
            i+=1
            sleep(10)
        self.mqtt.clientClose()
        logging.info("Finished Publishing")
        return True
    
    #Method for evaluating the sensor values and create decision for actuation  
    def handleActuatorData(self,SensorData):
        self.actuator.max_value = SensorData.max_value
        self.actuator.min_value = SensorData.min_value
        self.actuator.readings_number = SensorData.readings_number
        self.actuator.value  = SensorData.getCurrentValue()
        self.actuator.avgTemp = (SensorData.total_value / SensorData.readings_number)
        self.actuator.total_value = SensorData.total_value
        self.actuator.setName(SensorData.getName())      
        self.actuatorOP.updateActuator(self.actuator)
        return True