'''
Created on Apr 9, 2020

@author: Siddhartha
'''
import logging
import threading
from time import sleep
from project.ArduinoManager import ArduinoManager
from project import SystemPerformanceAdaptor,MqttClientConnector
from labs.common.PlantDeviceSensorData import PlantDeviceSensorData
from labs.common.DataUtil import DataUtil

class DeviceDataManager():
    #Constructor
    def __init__(self):
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        self.ard = ArduinoManager.getInstance()
        self.mqttP = MqttClientConnector.MqttClientConnector()
        self.mqttS = MqttClientConnector.MqttClientConnector()
        self.pdsd = PlantDeviceSensorData()
    #App initialization method   
    def run(self):
        t1 = threading.Thread(target=self.dataPublish,args=())
        t2 = threading.Thread(target=self.actuatorCommand,args=())
        t1.start()
        t2.start()
    #Method to collect data from various sources and pushing it to mqtt    
    def dataPublish(self):
        logging.info("------------------Starting sensor reader---------------\n")
        while(True):
            self.pdsd.setLdr(self.ard.getLdrValues())
            logging.info("LDR data received from arduino " + str(self.pdsd.getLdr()))
            self.pdsd.setSoilMoisture(self.ard.getSoilMoistureValues())
            logging.info("Soil Moisture data received from arduino " + str(self.pdsd.getSoilMoisture()))
            self.pdsd.setConstrainMemoryUtil(SystemPerformanceAdaptor.getSystemMemoryUtil())
            logging.info("Constrain Device System Memory Util " + self.pdsd.getConstrainMemoryUtil())
            self.pdsd.setConstrainCpuUtil(SystemPerformanceAdaptor.getSystemCpuUtil())
            logging.info("Constrain Device System CPU Util " + self.pdsd.getConstrainCpuUtil())
            self.pdsd.setHumidity(self.ard.getHumidity())
            logging.info("Humidity data received " + str(self.pdsd.getHumidity()))
            self.pdsd.setTemperature(self.ard.getTemperature())
            logging.info("Temperature data received " + str(self.pdsd.getTemperature()))
            json = DataUtil.toJsonFromPlantDeviceSensorData(self.pdsd)
            logging.info("Sending data to gateway\n"+json)
            self.mqttP.publishMqtt(json)
            logging.info("Data sent to broker")
            sleep(120)
    #Method to start mqtt with Ubidots to losten for actuator command
    def actuatorCommand(self):
        logging.info("------------------Starting MQTT subscriber---------------\n")
        self.mqttS.subscribeMqtt()    