'''
Created on Feb 15, 2020

@author: Siddhartha
'''
from sense_hat import SenseHat
from labs.common.SensorData import SensorData
from labs.module04 import SensorDataManager
from time import sleep
import logging

import smbus

#

class I2CSensorAdaptorTask:
    
    def __init__(self):
        self.sdm = None
        self.sensorData = None
        self.i2cBus = smbus.SMBus(1)
        self.humidAddr = 0x5F # address for humidity sensor
        self.bits = 8
        self.i2cBus.write_byte_data(self.humidAddr, 0, 0)
    #Method to implement lazy object initialization    
    def objectLoader(self):
        self.sensorData = SensorData()
        self.sensorData.setName("HumidityI2C")
        self.sdm = SensorDataManager.SensorDataManager()    
    #Method for fetching the sensor value from senseHat I2C module     
    def displayHumidityData(self):
        coeffH0 = self.i2cBus.read_byte_data(self.humidAddr, 0x30)
        coeffH1 = self.i2cBus.read_byte_data(self.humidAddr, 0x31)
        H0_rH= float(coeffH0/2.0)
        H1_rH  = float(coeffH1/2.0)                  
        #print("H0_RH = " + str(H0_rH))
        #print("H1_rH = " + str(H1_rH))
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
        #print("H1_T0_OUT = " + str(H1_TO_OUT))         
        rawH1T1a  = self.i2cBus.read_byte_data(self.humidAddr, 0x28)
        rawH1T1b  = self.i2cBus.read_byte_data(self.humidAddr, 0x29)
        H_T_OUT   = (rawH1T1b<<self.bits) | rawH1T1a
        if H_T_OUT & (1 << 16 - 1):
            H_T_OUT -= (1 << 16)
        hper =  float(((H1_rH-H0_rH)*(H_T_OUT-H0_T0_OUT))/(H1_TO_OUT-H0_T0_OUT))+H0_rH
        self.sensorData.addValue(hper)
        return self.sensorData.current
        #print("I2C Humidity = " + str(Ih) + "%")
    #Method to push data to SensorDataManger
    def pushData(self):
        self.sdm.hadleSensorData(self.sensorData)
            

