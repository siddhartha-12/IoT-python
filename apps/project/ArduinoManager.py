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
    #Uncomment the below code for I2C
        '''
        coeffH0 = self.i2cBus.read_byte_data(self.humidAddr, 0x30)
        coeffH1 = self.i2cBus.read_byte_data(self.humidAddr, 0x31)
        H0_rH= float(coeffH0/2.0)
        H1_rH  = float(coeffH1/2.0)                  
        valH0T0a  = self.i2cBus.read_byte_data(self.humidAddr, 0x36)
        valH0T0b  = self.i2cBus.read_byte_data(self.humidAddr, 0x37)
        H0_T0_OUT   =  (valH0T0b<<self.bits ) | valH0T0a
        if H0_T0_OUT & (1 << 16 - 1):
            H0_T0_OUT -= (1 << 16)
        #print("H0_T0_OUT = " + str(H0_T0_OUT))
        valH1T1a  = self.i2cBus.read_byte_data(self.humidAddr, 0x3A)
        valH1T1b  = self.i2cBus.read_byte_data(self.humidAddr, 0x3B)
        H1_TO_OUT   = (valH1T1b<<self.bits ) | valH1T1a
        if H1_TO_OUT & (1 << 16 - 1):
            H1_TO_OUT -= (1 << 16)       
        rawH1T1a  = self.i2cBus.read_byte_data(self.humidAddr, 0x28)
        rawH1T1b  = self.i2cBus.read_byte_data(self.humidAddr, 0x29)
        H_T_OUT   = (rawH1T1b<<self.bits) | rawH1T1a
        if H_T_OUT & (1 << 16 - 1):
            H_T_OUT -= (1 << 16)
        hper =  float(((H1_rH-H0_rH)*(H_T_OUT-H0_T0_OUT))/(H1_TO_OUT-H0_T0_OUT))+H0_rH
        return hper
    '''
    #Method to issue commands to Servo motor
    def servoCommand(self):
        logging.info("Issuing command to water")
        self.ser.write(b's')
        return True
        
        
    