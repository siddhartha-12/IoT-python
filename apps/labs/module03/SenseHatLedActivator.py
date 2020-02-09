'''
Created on Feb 9, 2020

@author: Siddhartha
'''
import logging
from sense_hat import SenseHat

class SenseHatLedActivator:
    
    def __init__(self):
        self.hat = SenseHat()
    
    def updateLed(self,msg):
        self.hat.show_message(msg)
        #logging.info("Updating Led " + msg)
        