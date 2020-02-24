'''
Created on Feb 21, 2020

@author: Siddhartha
'''
from labs.common.ActuatorData import ActuatorData
from labs.common.SensorData import SensorData
from labs.common.DataUtil import DataUtil
import redis,logging
from labs.common.ActuatorDataListener import ActuatorDataListener

class PersistenceUtil:
    def __init__(self):
        self.host = "redis-11821.c114.us-east-1-4.ec2.cloud.redislabs.com"
        self.port = 11821
        self.auth = "connected2020"
        
    def registerSensorDataDbmsListener(self):
        db = redis.StrictRedis(host=self.host, port=self.port, password=self.auth, decode_responses=True)
        dbs = db.pubsub()
        dbs.subscribe("Sensor")
        
    def registerActuatorDataDbmsListener(self,ActuatorDataListener):
        db = redis.StrictRedis(host=self.host, port=self.port, password=self.auth, decode_responses=True)
        dbs = db.pubsub()
        dbs.subscribe("Actuator")
        #logging.info("Waiting for message")
        for new_message in dbs.listen():
            adj = db.get(new_message['data'])
            #logging.info("Received new message" + str(new_message['data']))
            if(new_message['data']!=1):
                logging.info("New Actuator Reading Received with ID \n" + str(new_message['data']))
                #logging.info("New Actuator Data Received - " + adj )
                ad = DataUtil.toActuatorDataFromJson(self, adj)
                ActuatorDataListener.onActuatorMessage(ad)
        
    def writeSensorToDataDbms(self,SensorData):
        dbData = DataUtil.toJsonFromSensorData(SensorData)
        r = redis.StrictRedis(host=self.host, port=self.port, password=self.auth, decode_responses=True)
        r.set("Sensor"+SensorData.getTimeStamp(),dbData)
        r.publish("Sensor", "Sensor"+SensorData.getTimeStamp())
        #logging.info("Sending data to DB")    
        
    def writeActuatorToDataDbms(self,ActuatorData):
        dbData = DataUtil.toJsonFromSensorData(SensorData)
        r = redis.StrictRedis(host=self.host, port=self.port, password=self.auth, decode_responses=True)
        #r.set(SensorData.getTimeStamp()+"- Sensor",dbData)
        r.publish("Actuator", dbData)
        #logging.info("Sending data to DB") 