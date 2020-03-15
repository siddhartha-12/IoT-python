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
        
#      /***
#      * Method for initializationa and make Mqtt Client connection with the broker.
#      * Setting callback to self as the CallBack class has been extended to this class
#      * @return true
#      */       
        
    def connect(self):
        self.client.connect(self.host, self.port)  
        return True
    #Method to send actuator data on the mqtt channel
    def publishActuatorCommand(self,ActuatorData,qosq):
        message = ActuatorData
        self.client.publish("Connected-Device/Actuator_Data", message, qos=qosq)
        logging.info("Actuator Data published to - >",)
        return True
    #Method to send sensor data on the mqtt channel
    def publishSensorData(self,SensorData,qosq):
        message = SensorData 
        self.client.publish("Siddhartha/Connected-Device/Sensor_Data", message, qos=qosq)
        logging.info("Sensor Data published to - >")
        return True
    #Method to subscribe to actuator channel
    def subscribeToActuatorCommands(self,ActuatorDataListener):
        return True
    #Method to subscribe to sensor channel
    def subscribeToSensorMessages(self,SensorDataListener):
        self.client.subscribe("Connected-Device/Sensor_Data", qos=1)
        self.client.on_message = self.MessageReceived
        logging.info()
#     /***
#      * Callback function on when the message arrives
#      */
    def MessageReceived(self,MQTTMessage):
        return True
#Method to close mqtt connection    
    def clientClose(self):
        self.client.disconnect()
        return True
        
    
    
    
    
    # 