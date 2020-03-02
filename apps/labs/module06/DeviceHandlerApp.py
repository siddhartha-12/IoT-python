'''
Created on Jan 30, 2020

@author: Siddhartha
'''
from labs.module06.DeviceDataManager import DeviceDataManager
import logging

#Entry level script
# Starts the application
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
DeviceAdapter = DeviceDataManager();
#setting the thread and executing
DeviceAdapter.run()



