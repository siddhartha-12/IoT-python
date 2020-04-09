from labs.module07.HumiditySensorAdaptorTask import HumiditySensorAdaptorTask
#Threaded Class
class MultiSensorAdaptor :
    #Default Constructor
    def __init__(self):
        self.sreader = HumiditySensorAdaptorTask() 
    #Fetch current readings from the sensor
    def getSensorData(self):
        self.sreader.objectLoader()
        sensorRead = self.sreader.readSensorValue()
        return sensorRead

    