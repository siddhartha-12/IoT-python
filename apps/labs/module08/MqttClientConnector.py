'''
Created on Feb 29, 2020

@author: Siddhartha
'''
import paho.mqtt.client as mqtt
import logging
class MqttClientConnector:
    mqttc = None
    def __init__(self):
        self.mqttc = mqtt.Client()
        
    def on_connect(self,mqttc, obj, flags, rc):
        logging.info("Connected to broker")
        return True
    
    def on_disconnect(self,mqttc, obj, flags, rc):
        logging.info("disconnected to broker")
        return True

    def on_message(self,mqttc, obj, msg):
        logging.info(msg.topic + " Actuator Value changed to " + msg.payload.decode("utf-8"))
    
    def on_publish(self,mqttc, obj, mid):
        logging.info("mid: " + str(mid))
            
    def on_subscribe(self,mqttc, obj, mid, granted_qos):
        logging.info("Subscribed: ActuatorData/change ")
    
    def on_log(self,mqttc, obj, level, string):
        logging.info(string)

    def connectMqtt(self):
        self.mqttc.on_message = self.on_message
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_publish = self.on_publish
        self.mqttc.on_subscribe = self.on_subscribe
        # Uncomment to enable debug messages
        # mqttc.on_log = on_log
        self.mqttc.connect("mqtt.eclipse.org", 1883, 60)
        self.mqttc.subscribe("ActuatorData/change", 0)
        self.mqttc.loop_forever()
        
    def clientDisconnect(self):
        self.mqttc.disconnect(None, None)
        return True
        