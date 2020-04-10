'''
Created on Apr 9, 2020

@author: Siddhartha
'''
import logging
from project.ArduinoManager import ArduinoManager
from project import SystemPerformanceAdaptor,MqttClientConnector
import threading
from time import sleep
from pip._internal import self_outdated_check

class DeviceDataManager():
    def __init__(self):
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        self.ard = ArduinoManager.getInstance()
        self.mqttP = MqttClientConnector.MqttClientConnector()
        self.mqttS = MqttClientConnector.MqttClientConnector()
        
    def run(self):
        t1 = threading.Thread(target=self.dataPublish,args=())
        t2 = threading.Thread(target=self.actuatorCommand,args=())
        t1.start()
        t2.start()
        
    
    def dataPublish(self):
        logging.info("------------Starting sensor reader-----------------")
        while(True):
            arduino = self.ard.getArduinoValues()
            logging.info("Data received from arduino " + str(arduino))
            sysUtil = SystemPerformanceAdaptor.getSystemUtil()
            logging.info("Constrain Device System Util " + sysUtil)
            json = arduino + "," + sysUtil
            logging.info("Ready to send json -> " + json)
            self.mqttP.publishMqtt(json)
            logging.info("Data sent to broker")
            sleep(60)
    
    def actuatorCommand(self):
        logging.info("------------------Starting MQTT subscriber---------------")
        self.mqttS.subscribeMqtt()
        
        