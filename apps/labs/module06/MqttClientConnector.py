'''
Created on Feb 29, 2020

@author: Siddhartha
'''
from labs.common.ActuatorData import ActuatorData
from labs.common.SensorData import SensorData
from labs.common.ConfigUtil import ConfigUtil
#from labs.common.ActuatorDataListener import ActuatorDataListener
#from labs.common import SensorDataListener
from paho.mqtt.client import MQTTMessage
import logging
import paho.mqtt.client as paho
from labs.common.DataUtil import DataUtil


class MqttClientConnector:
    def __init__(self):
        config = ConfigUtil();
        config.loadConfig("../../../config/ConnectedDevicesConfig.props")
        self.host = config.getValue("mqtt.cloud", "host")
        self.port = int(config.getValue("mqtt.gateway", "port"))
        self.client = paho.Client("SiddharthaIoTp")
        
        
        
    def connect(self):
        self.client.connect(self.host, self.port)  
        return True
    
    def publishActuatorCommand(self,ActuatorData,qosq):
        message = ActuatorData
        self.client.publish("Connected-Device/Actuator_Data", message, qos=qosq)
        logging.info("Actuator Data published to - >",)
        return True
    
    def publishSensorData(self,SensorData,qosq):
        message = SensorData 
        self.client.publish("Siddhartha/Connected-Device/Sensor_Data", message, qos=qosq)
        logging.info("Sensor Data published to - >")
        return True
    
    def subscribeToActuatorCommands(self,ActuatorDataListener):
        return True
    
    def subscribeToSensorMessages(self,SensorDataListener):
        self.client.subscribe("Connected-Device/Sensor_Data", qos=1)
        self.client.on_message = self.MessageReceived
        logging.info()
    
    def MessageReceived(self,MQTTMessage):
        return True
    
    def registerActuatorDataListener(self,ActuatorDataListener):
        return True
    
    def registerSensorDataListener(self,SensorDataListener):
        return True
    
    def clientClose(self):
        self.client.disconnect()
        return True
        
    
    
    
    
    # 