'''
Created on Jan 30, 2020

@author: Siddhartha
'''
from labs.module03.SensorDataManager import SensorDataManager
from labs.common.ConfigUtil import ConfigUtil
import logging

#Entry level script

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
tempAdapter = SensorDataManager();
#setting the thread and executing
tempAdapter.run()



