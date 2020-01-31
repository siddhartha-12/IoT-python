'''
Created on Jan 30, 2020

@author: Siddhartha
'''
from labs.module02.TempSensorEmulatorTask import TempSensorEmulatorTask
import logging
import threading
from time import sleep

class TempEmulatorAdaptor:
    def run(self):
        #print("Starting at console")
        logging.info("Starting application")
        tempTask = TempSensorEmulatorTask()
        #tempTask.sendNotification()
        i = 0;
#         t1 = threading.Thread(tempTask.sendNotification())
#         t1.start()
        while(i<11):
            tempTask.sendNotification()
            i+=1
            sleep(5)
            