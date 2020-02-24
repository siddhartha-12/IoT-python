'''
Created on Jan 30, 2020

@author: Siddhartha
'''
from labs.module05.DeviceDataManager import DeviceDataManager
from labs.common.ConfigUtil import ConfigUtil
import logging

#Entry level script
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
DeviceAdapter = DeviceDataManager();
#setting the thread and executing
DeviceAdapter.run()



