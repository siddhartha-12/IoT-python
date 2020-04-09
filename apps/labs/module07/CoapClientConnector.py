'''
Created on Feb 29, 2020

@author: Siddhartha
'''
import getopt
import socket
import sys
from labs.common.ActuatorData import ActuatorData
from labs.common.SensorData import SensorData
from labs.common.ConfigUtil import ConfigUtil
import logging
from coapthon.client.helperclient import HelperClient 
from coapthon.messages import response

class CoapClientConnector:
    def __init__(self):
        config = ConfigUtil();
        config.loadConfig("../../../config/ConnectedDevicesConfig.props")
        self.host = config.getValue("coap.device", "host")
        self.port = int(config.getValue("coap.device", "port"))     
        self.path ="Temp"
        self.client = HelperClient(server=(self.host, self.port))
#      /***
#      * Method for starting the COAP server.
#      * Executing All the Methods GET,PUT,POST and DELETE
#      * @return true
#      */             
    def send(self,data):
        try:
            self.put(data)
            self.get()
            self.post(data)
            self.delete()
            self.client.stop()
            return True
        except:
            return False
    #Method to call post method for coap
    def post(self,data):
        try:
            response=self.client.post(self.path, data)
            logging.info("Received Response Post-> " +response.pretty_print())
            return True
        except:
            return False
        #Method to call put method for coap
    def put(self,data):
        try:
            response=self.client.put(self.path, data)
            logging.info("Received Response Post-> " +response.pretty_print())
            return True
        except:
            return False
    #Method to call get method for coap
    def get(self):
        try:
            response = self.client.get(self.path)
            logging.info("Received Response GET-> " +response.pretty_print())
            logging.info(response.Message.payload)
            return True
        except:
            return False
        #Method to call delete method for coap
    def delete(self):
        try:
            response = self.client.delete(self.path)
            logging.info("Received Response delete-> " +response.pretty_print())
            return True
        except:
            return False