'''
Created on Jan 30, 2020

@author: Siddhartha
'''
from labs.module02.TempEmulatorAdaptor import TempEmulatorAdaptor
from labs.common.ConfigUtil import ConfigUtil
import logging
import threading



logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
tempAdapter = TempEmulatorAdaptor();
t1 = threading.Thread(tempAdapter.run())
t1.setDaemon(True)
t1.start()



