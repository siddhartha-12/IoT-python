'''
Created on Jan 20, 2020

@author: Siddhartha
'''
import logging

from time import sleep
from labs.module01 import SystemPerformanceAdaptor
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
logging.info("Starting system performance app ")
i=0;
while (i<15):
    SystemPerformanceAdaptor.run()
    i+=1
    sleep(5)
    
