'''
Created on Apr 9, 2020

@author: Siddhartha
'''
from project.PortManager import PortManager
import serial as sl
import logging
from time import sleep
from builtins import staticmethod
from sense_hat import SenseHat
class ArduinoManager():
    __instance = None
    '''
    Implementing Singleton to have a single instance of the arduino connection to avoid override and conflict
    '''
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if ArduinoManager.__instance == None:
            logging.info("Creating first Arduino Manager instance")
            ArduinoManager()
        return ArduinoManager.__instance      
    #Constructor
    def __init__(self):
        ArduinoManager.__instance = self
        self.portNumber = PortManager.getArduinoPort()
        self.ser = sl.Serial(self.portNumber,9600)
        self.sensehat =  SenseHat()
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("Sending Arduino Instance")
    #Method to get LDR values   
    def getLdrValues(self):
        sleep(2)
        while(True):
            logging.info("Connecting to Arduino")        
            self.ser.write(b'a') #Send data to arduino. Activate arduino read pin and write to serial  
            logging.info("Requested data from Arduino...waiting for response")
            data = self.ser.readline();
            return(str(data.decode("utf-8")).rstrip("\n\r"))
    #Method to get Soil Moisture values
    def getSoilMoistureValues(self):
        sleep(2)
        while(True):
            logging.info("Connecting to Arduino")        
            self.ser.write(b'b') #Send data to arduino. Activate arduino read pin and write to serial  
            logging.info("Requested data from Arduino...waiting for response")
            data = self.ser.readline();
            return(str(data.decode("utf-8")).rstrip("\n\r"))
    #Method to get Temperature value        
    def getTemperature(self):
        return(self.sensehat.get_temperature())
    #Method to get humidity values
    def getHumidity(self):
        return(self.sensehat.get_humidity())
    #Method to issue commands to Servo motor
    def servoCommand(self):
        logging.info("Issuing command to water")
        self.ser.write(b's')
        return True
        
        
    