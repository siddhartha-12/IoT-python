import unittest
from labs.module04.MultiActuatorAdaptor import MultiActuatorAdaptor
from labs.common.ActuatorData import ActuatorData
from labs.module04.SensorDataManager import SensorDataManager
from labs.common.SensorData import SensorData
from labs.module04.HumiditySensorAdaptorTask import HumiditySensorAdaptorTask
from labs.module04.SenseHatLedActivator import SenseHatLedActivator
from labs.module04.MultiSensorAdaptor import MultiSensorAdaptor
from labs.module04.SenseHatLedActivator import SenseHatLedActivator


"""
Test class for all requisite Module04 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class Module04Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.sd = SensorData()
		self.sd.addValue(11)
		self.sd.setName("Test")
		self.sdm = SensorDataManager()
		self.sdm.actuator.addValue(11)
		self.actuator = ActuatorData();
		self.actuator.addValue(2)
		self.actuator.setName("Test")
		self.tsa = MultiSensorAdaptor()
		self.taa = MultiActuatorAdaptor()
		self.tat = HumiditySensorAdaptorTask()
		self.tat.sensorData = SensorData()
		self.shla = SenseHatLedActivator()
		

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		pass

	"""
	Place your comments describing the test here.
	"""
	'@Test'
	def testSendNotification(self):
		self.assertTrue(self.sdm.sendNotification(), "Notification Unsucessful")
		pass
	'@Test'
	def testhadleSensorData(self):
		self.assertTrue(self.sdm.hadleSensorData(self.sd), "Sensor handle data method not working")
	'@Test'	
	def testgetSensorData(self):
		self.assertTrue(self.tsa.getSensorData(),"Issue in temperature adaptor")
	'@Test'
	def testreadSensorValueMin(self):
		self.assertGreaterEqual(self.tat.readSensorValue(),0.0,'sensor value coming less than 0')
		self.assertGreaterEqual(100,self.tat.readSensorValue(),'sensor value coming more than 100')
	
	'@Test'	
	def testupdateActuator(self):
		self.assertTrue(self.taa.updateActuator(self.actuator), "Actuator update failed")	
	'@Test'
	def testupdateLed(self):
		self.assertTrue(self.shla.updateLed("Test Message"),"Led update failed")
	
	'@Test'
	def testreadSensorValuePushNotification(self):
		self.tat.sensorData=SensorData()
		self.tat.sensorData.addValue(12)
		self.tat.sensorData.setName("Test")
		self.tat.sdm = SensorDataManager()
		self.assertTrue(self.tat.pushData(),"Message not getting pushed to Sensor Data Manager")

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()