'''
Created on Apr 9, 2020

@author: Siddhartha
'''
import serial.tools.list_ports


class PortManager:

    @staticmethod
    def getArduinoPort():
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            if(desc[0:7] == "Arduino"):
                return port

