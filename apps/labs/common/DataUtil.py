'''
Created on Feb 21, 2020

@author: Siddhartha
'''
from labs.common.ActuatorData import ActuatorData
from labs.common.SensorData  import SensorData  

import json
import logging
from builtins import staticmethod


class DataUtil:
    
    @staticmethod        
    def toJsonFromSensorData(sensorData):
        s = json.dumps(sensorData.__dict__)
        logging.info("New Sensor reading \n" + s)
        return s
        
#     def toSensorDataFromJson(self)
#     def toSensorDataFromJsonFile(self)
    @staticmethod
    def toJsonFromActuatorData(self,actuatorData):
        a = json.dumps(actuatorData.__dict__)
        logging.info(a)
    @staticmethod     
    def toActuatorDataFromJson(self,string):
        act = ActuatorData()
        data = json.loads(string)
        logging.info(data)
        act.name = data['name']
        act.value = data['current']
        act.command = data['command']
        act.min_value = data['min_value']
        act.max_value = data['max_value']
        act.total_value = data['total_value']
        act.avgTemp = data['avgTemp']
        act.timestamp = data['timestamp']
        logging.info("New actuator generated from JSon \n")       
        return act
#     def toActuatorDataFromJsonFile(self)
#     def writeActuatorDataToFile(self,ActuatorData)
#     def writeSensorDataToFile(self,SensorData)    