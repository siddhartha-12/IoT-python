import unittest
from project.ArduinoManager import ArduinoManager
from project import SystemPerformanceAdaptor,MqttClientConnector
from project.PortManager import PortManager

"""
Test class for all requisite Project functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class ProjectTest(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.ard = ArduinoManager.getInstance()
		self.mqttP = MqttClientConnector.MqttClientConnector()
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
	def testArduinoInstance(self):
		self.assertIsNotNone(ArduinoManager.getInstance(), "Instance fetch failed") 
		pass
	def testGetLdrValues(self):
		self.assertIsNotNone(self.ard.getLdrValues(), "LDR value failed")
		pass
	def testGetSoilMoistureValues(self):
		self.assertIsNotNone(self.ard.getSoilMoistureValues(), "moisture value failed")
		pass
	def testGetTemperature(self):
		self.assertIsNotNone(self.ard.getHumidity(), "temperature value failed")
		pass
	def testGetHumidity(self):
		self.assertIsNotNone(self.ard.getTemperature(), "Humidity value failed")
		pass
	def testServoCommand(self):
		self.assertTrue(self.ard.servoCommand(), "Servo value failed")
		pass
	def testGetCpuUtil(self):
		self.assertIsNotNone(SystemPerformanceAdaptor.getSystemCpuUtil(), "Cpu Util value failed")
		pass
	def testGetMemoryUtil(self):
		self.assertIsNotNone(SystemPerformanceAdaptor.getSystemMemoryUtil(), "Memory Util value failed")
		pass
	def testGetPorts(self):
		self.assertIsNotNone(PortManager.getArduinoPort(), "Did not find ports value failed")
		pass

	

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()