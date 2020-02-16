import logging
from labs.module02.SmtpClientConnector import SmtpClientConnector
from labs.module04.MultiSensorAdaptor import MultiSensorAdaptor
from labs.module04.MultiActuatorAdaptor import MultiActuatorAdaptor
from labs.common.ActuatorData import ActuatorData
from labs.common.SensorData import SensorData
from labs.common.ConfigUtil import ConfigUtil


class SensorDataManager:
    #Default Constructor
    def __init__(self):
        self.actuator = ActuatorData();
        self.sensorAdaptor = MultiSensorAdaptor()
        self.config = ConfigUtil()
        self.config.loadConfig("../../../config/ConnectedDevicesConfig.props")
        self.threshold = float(self.config.getValue("device", "nominalTemp"))
        self.actuatorOP = MultiActuatorAdaptor.getInstance()
        
    def run(self):
        
        self.sensorAdaptor.getSensorData()
    #Method for evaluating the sensor values and create decision for actation  
    def hadleSensorData(self,SensorData):
        self.actuator.max_value = SensorData.max_value
        self.actuator.min_value = SensorData.min_value
        self.actuator.readings_number = SensorData.readings_number
        self.actuator.value  = SensorData.getCurrentValue()
        self.actuator.avgTemp = (SensorData.total_value / SensorData.readings_number)
        self.actuator.total_value = SensorData.total_value
        self.actuator.setName(SensorData.getName())      
        self.actuatorOP.updateActuator(self.actuator)
        print("Value check - " + str(self.actuator.value))
        self.sendNotification()
        return True
    
     #Triggering mail based on the command value. The mail contains the relevant information.
    def sendNotification(self):
        
        try:
            logging.info(self.actuator.getName()+"Temperature: \nTime: "+str(self.actuator.timestamp)+" Value :"+str(self.actuator.getValue()))
            mail = SmtpClientConnector()
            #Creating mail body text
            data = "Reading from:"+self.actuator.getName()+ "Time: "+str(self.actuator.timestamp)+"\ncurrent : "+str(self.actuator.getValue()) +"\nAverage :"+str(self.actuator.getAverageValue())+"\nSamples :"+str(self.actuator.readings_number)+"\nMin: "+str(self.actuator.min_value)+"\nMax :"+str(self.actuator.max_value)
            mail.publishMessage("Temperature Alert Python -"+self.actuator.getName(), data)
            logging.info('\nMail sent')
            return True
        except Exception as e:
            logging.info(e)
            #If the mailing fails, the method returns false
            return False