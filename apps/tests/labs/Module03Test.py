import unittest
from labs.module03.TempActuatorAdaptor import TempActuatorAdaptor
from labs.common.ActuatorData import ActuatorData
from labs.module03.SensorDataManager import SensorDataManager
from labs.common.SensorData import SensorData
from labs.module03.TempSensorAdaptorTask import TempSensorAdaptorTask
from labs.module03.TempActuatorAdaptor import TempActuatorAdaptor
from labs.module03.SenseHatLedActivator import SenseHatLedActivator
from labs.module03.TempSensorAdaptor import TempSensorAdaptor
from labs.module03.SenseHatLedActivator import SenseHatLedActivator
"""
Test class for all requisite Module03 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class Module03Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.sd = SensorData()
		self.sd.addValue(11)
		self.sdm = SensorDataManager()
		self.actuator = ActuatorData();
		self.actuator.setCommand("Raise Temp")
		self.sdm.threshold = 20
		self.tsa = TempSensorAdaptor()
		self.taa = TempActuatorAdaptor()
		self.tat = TempSensorAdaptorTask()
		self.shla = SenseHatLedActivator()
		
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
	'@Test'
	def testreadSensorValueMax(self):
		self.assertGreaterEqual(100,self.tat.readSensorValue(),'sensor value coming more than 100')
	'@Test'	
	def testupdateActuator(self):
		self.assertTrue(self.taa.updateActuator(self.actuator), "Actuator update failed")	
	'@Test'
	def testupdateLed(self):
		self.assertTrue(self.shla.updateLed("Test Message"),"Led update failed")
		
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()