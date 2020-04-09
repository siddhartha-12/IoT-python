'''
Created on Feb 29, 2020

@author: Siddhartha
'''
from labs.module07.DeviceDataManager import DeviceDataManager
import logging
from labs.module07.CoapClientConnector import CoapClientConnector
    #Entry level script
    # Starts the application
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
DeviceAdapter = DeviceDataManager();
    #setting the thread and executing
DeviceAdapter.run()

