import unittest
from labs.module05.SenseHatLedActivator import SenseHatLedActivator

from labs.common.ActuatorData import ActuatorData
from labs.module05.HumiditySensorAdaptorTask import HumiditySensorAdaptorTask
from labs.module05.PersistenceUtil import PersistenceUtil
from labs.common.SensorData import SensorData

"""
Test class for all requisite Module05 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
import sense_hat
class Module05Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		
		self.ac = ActuatorData()
		self.ac.addValue(15)
		self.sensor = SensorData()
		self.sensor.addValue(15)
		self.hsa = HumiditySensorAdaptorTask()
		self.hsa.objectLoader()
		self.pu = PersistenceUtil()
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
	def testSenseHatActivator(self):
		hat = SenseHatLedActivator()
		self.assertTrue(hat.updateLed("Test"),"Led Update Failed")
		pass
	
	def testSensorData(self):
		a = self.hsa.readSensorValue()
		self.assertGreaterEqual(a.current, 0, "Issue with sensor")
		pass
	
	def testWriteActuator(self):
		self.assertTrue(self.pu.writeActuatorToDataDbms(self.ac))
		pass
 	
	def testWriteSensor(self):
		self.assertTrue(self.pu.writeSensorToDataDbms(self.sensor))
		pass
		

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()