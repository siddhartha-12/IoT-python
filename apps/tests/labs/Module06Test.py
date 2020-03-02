import unittest


"""
Test class for all requisite Module06 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
from labs.module05.DeviceDataManager import DeviceDataManager
from labs.module06.MqttClientConnector import MqttClientConnector
from labs.common.SensorData import SensorData
from labs.common.ActuatorData import ActuatorData
from paho.mqtt.client import MQTTMessage

class Module06Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.ddm = DeviceDataManager();
		self.ddm.actuator.addValue(15)
		self.mqt = MqttClientConnector();
		self.sd = SensorData();
		self.sd.addValue(14)
		mm = MQTTMessage()
		mm.payload = "ss" 
		pass

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		pass

	"""
	Place your comments describing the test here.
	"""

	def testconnect(self):
		self.assertTrue(self.mqt.connect(), "Connection Failed")
		pass
	
# 	def testpublishActuatorCommand(self):
# 		ac = ActuatorData();
# 		ac.addValue(14)
# 		self.assertTrue(self.mqt.publishActuatorCommand(ac,1), "publishActuator Failed")
# 		pass
	
	def testpublishSensorData(self):
		self.assertTrue(self.mqt.publishSensorData(self.sd, 1), "publishSensor Failed")
		pass
	
	def testMessageReceived(self):
		self.assertTrue(self.mqt.MessageReceived(MQTTMessage), "Message Failed")
		pass
	
	def testClientClose(self):
		self.assertTrue(self.mqt.clientClose(), "Client connection close Failed")
		pass

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()