'''
Created on Jan 30, 2020

@author: Siddhartha
'''
from labs.common.SensorData import SensorData
from labs.module02.SmtpClientConnector import SmtpClientConnector
import logging
from email.policy import SMTP
class TempSensorEmulatorTask :
    minTemp = 0
    maxTemp = 0
    currentTemp = 0
    avgTemp = 0
    threshold = 5
    sensor = None

    def __init__(self):
        self.sensor = SensorData();

    #Fetch current readings from the sensor
    def getSensorData(self):
        
        self.currentTemp = self.sensor.getCurrentValue()
        self.minTemp = self.sensor.getMinValue()
        self.maxTemp = self.sensor.getMaxValue()
        self.avgTemp = self.sensor.getAverageValue()
        self.readings = self.sensor.getCount()
        logging.info("\n \nTemperature: \nTime: "+str(self.sensor.timestamp)+"\ncurrent : "+str(self.currentTemp) +"\nAverage :"+str(self.avgTemp)+"\nSamples :"+str(self.readings)+"\nMin: "+str(self.minTemp)+"\nMax :"+str(self.maxTemp)+"\n")
        return self.currentTemp
    #Testing if the threshold has been breached. If breached a mail has been triggered
    def sendNotification(self):
        try:
            self.getSensorData()
            if(abs(self.currentTemp - self.avgTemp) > self.threshold):
                logging.info('Current temp exceeds average beyond ' + str(self.threshold) + '. Triggering alert...')
                mail = SmtpClientConnector()
                #Creating mail body text
                data = "Temperature Exceeded Warning!\n \nTemperature: \nTime: "+str(self.sensor.timestamp)+"\ncurrent : "+str(self.currentTemp) +"\nAverage :"+str(self.avgTemp)+"\nSamples :"+str(self.readings)+"\nMin: "+str(self.minTemp)+"\nMax :"+str(self.maxTemp)
                mail.publishMessage("Temperature Alert Python", data)
                logging.info('\nMail sent')
            return True
        except:
            #If the mailing fails, the method returns false
            return False