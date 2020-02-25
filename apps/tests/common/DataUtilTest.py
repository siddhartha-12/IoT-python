import unittest
from labs.common.SensorData import SensorData
from labs.common.DataUtil import DataUtil
from labs.common.ActuatorData import ActuatorData
import logging
"""
Test class for all requisite DataUtil functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class DataUtilTest(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.du = DataUtil()
		self.sd = SensorData()
		self.sd.addValue(15)
		self.sd.setName("Test")
		self.ad =ActuatorData()
		self.ad.addValue(44)
		self.ad.setName("Test")
		self.ad.setCommand("Test")
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
	def testSomething(self):
		pass
	
	'@Test'
	def testCheckJsonData(self):
		jstring = self.du.toJsonFromSensorData(self.sd)
		#print(jstring)
		sd1  = self.du.toSensorDataFromJson(jstring)
		
		#print(str(self.sd.getCurrentValue()))
		#print(str(sd1.getCurrentValue()))
		self.assertTrue(self.sd.getCount()==sd1.getCount(), "count does not match")
		self.assertTrue(self.sd.getCurrentValue()==sd1.getCurrentValue(), "current does not match")
		pass
	
	'@Test'
	def testCheckActuatorData(self):
		jstring = self.du.toJsonFromActuatorData(self.ad)
		
	
	'@Test'
	def testtoActuatorDataFromJsonFile(self):
		self.assertTrue(self.du.toActuatorDataFromJsonFile(), "File to actuator failed")
		pass
	'@Test'
	def testwriteActuatorDataToFile(self):
		self.assertTrue(self.du.writeActuatorDataToFile(self.ad), "File to actuator failed")
		pass
	'@Test'
	def testwriteSensorDataToFile(self):
		self.assertTrue(self.du.toActuatorDataFromJsonFile(), "File to actuator failed")
		pass    

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()