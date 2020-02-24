'''
Created on Feb 9, 2020

@author: Siddhartha
'''
import logging
from sense_hat import SenseHat

class SenseHatLedActivator:
    #Default Constructor
    def __init__(self):
        self.hat = SenseHat()
    #Method for updating led display of sensehat
    def updateLed(self,msg):
        self.hat.show_message(msg)
        return True
        #logging.info("Updating Led " + msg)
        