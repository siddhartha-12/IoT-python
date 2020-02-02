'''
Created on Jan 30, 2020

@author: Siddhartha
'''
from labs.module02.TempSensorEmulatorTask import TempSensorEmulatorTask
import logging
from time import sleep

class TempEmulatorAdaptor:
    def run(self):
        logging.info("Starting application")
        tempTask = TempSensorEmulatorTask()
        i = 0;
        #Creating a while loop for taking 10 reading
        while(i<11):
            tempTask.sendNotification()
            i+=1
            sleep(5)
            