'''
Created on Mar 22, 2020

@author: Siddhartha
'''
from labs.module08.MqttClientConnector import MqttClientConnector
import logging
#Entry level script
# Starts the application
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
mcc = MqttClientConnector();
#setting the thread and executing
mcc.connectMqtt()



