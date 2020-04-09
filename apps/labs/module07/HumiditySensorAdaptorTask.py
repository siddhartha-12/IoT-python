from sense_hat import SenseHat
from labs.common.SensorData import SensorData
from time import sleep

class HumiditySensorAdaptorTask:
    #Default Constructor    
    def __init__(self):
        self.sensor = SenseHat()
        self.sensorData = SensorData()
        self.sdm = None
    #Method to implement lazy object initialization     
    def objectLoader(self):
        self.sensorData.setName("HumiditySenseHat")
    #Method for fetching the sensor value from senseHat module   
    def readSensorValue(self):
        humidity = self.sensor.get_humidity()
        self.sensorData.addValue(humidity)
        return self.sensorData