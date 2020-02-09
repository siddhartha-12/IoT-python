import logging
from labs.module02.SmtpClientConnector import SmtpClientConnector
from labs.module03.TempSensorAdaptor import TempSensorAdaptor
from labs.module03.TempActuatorAdaptor import TempActuatorAdaptor
from labs.common.ActuatorData import ActuatorData
from labs.common.SensorData import SensorData
from labs.common.ConfigUtil import ConfigUtil


class SensorDataManager:
    def __init__(self):
        self.actuator = ActuatorData();
        self.sensorAdaptor = TempSensorAdaptor()
        self.config = ConfigUtil()
        self.config.loadConfig("../../../config/ConnectedDevicesConfig.props")
        self.threshold = float(self.config.getValue("device", "nominalTemp"))
        self.actuatorOP = TempActuatorAdaptor()
        
    def run(self):
        
        self.sensorAdaptor.getSensorData()
        
    def hadleSensorData(self,SensorData):
        self.actuator.max_value = SensorData.max_value
        self.actuator.min_value = SensorData.min_value
        self.actuator.readings_number = SensorData.readings_number
        self.actuator.value  = SensorData.getCurrentValue()
        self.actuator.avgTemp = (SensorData.total_value / SensorData.readings_number)
        self.actuator.total_value = SensorData.total_value
        if(self.threshold>self.actuator.value):
            self.actuator.setCommand("Raise Temp")
            self.sendNotification()
        elif(self.threshold<self.actuator.value):
            self.actuator.setCommand("Decrease Temp")
        elif(self.threshold==self.actuator.value):
            self.actuator.setCommand("Temp Stable")
        self.actuatorOP.updateActuator(self.actuator)
        self.sendNotification()
    
     #Testing if the nominal temperature has been breached. If breached a mail has been triggered
    def sendNotification(self):
        
        try:
            if(self.actuator.getCommand()=="Raise Temp"):
                #logging.info('Current Temperature lower than threshold: ' + str(self.threshold) + ' Lowering Temp')
                logging.info("Current Temperature lower than threshold: \n \nTemperature: \nTime: "+str(self.actuator.timestamp)+"\ncurrent : "+str(self.actuator.getValue()) +"\nAverage :"+str(self.actuator. getAverageValue())+"\nSamples :"+str(self.actuator.readings_number)+"\nMin: "+str(self.actuator.min_value)+"\nMax :"+str(self.actuator.max_value))
                mail = SmtpClientConnector()
                #Creating mail body text
                data = "Current Temperature lower than threshold: \n \nTemperature: \nTime: "+str(self.actuator.timestamp)+"\ncurrent : "+str(self.actuator.getValue()) +"\nAverage :"+str(self.actuator.getAverageValue())+"\nSamples :"+str(self.actuator.readings_number)+"\nMin: "+str(self.actuator.min_value)+"\nMax :"+str(self.actuator.max_value)
                mail.publishMessage("Temperature Alert Python", data)
                logging.info('\nMail sent')
            
            elif(self.actuator.getCommand()=="Decrease Temp"):
                logging.info("Current Temperature higher than threshold: \n \nTemperature: \nTime: "+str(self.actuator.timestamp)+"\ncurrent : "+str(self.actuator.getValue()) +"\nAverage :"+str(self.actuator.getAverageValue())+"\nSamples :"+str(self.actuator.readings_number)+"\nMin: "+str(self.actuator.min_value)+"\nMax :"+str(self.actuator.max_value))
                mail = SmtpClientConnector()
                #Creating mail body text
                data = "Current Temperature higher than threshold: \n \nTemperature: \nTime: "+str(self.actuator.timestamp)+"\ncurrent : "+str(self.actuator.getValue()) +"\nAverage :"+str(self.actuator.getAverageValue())+"\nSamples :"+str(self.actuator.readings_number)+"\nMin: "+str(self.actuator.min_value)+"\nMax :"+str(self.actuator.max_value)
                mail.publishMessage("Temperature Alert Python", data)
                logging.info('\nMail sent')
            return True
        except Exception as e:
            logging.info(e)
            #If the mailing fails, the method returns false
            return False