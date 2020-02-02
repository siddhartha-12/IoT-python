import unittest
from labs.common.SensorData import SensorData


"""
Test class for all requisite SensorData functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class SensorDataTest(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	
	def setUp(self):
		self.sensor = SensorData()
		self.sensor.addValue(11)
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
	def testgetCurrent(self):
		self.assertGreaterEqual(self.sensor.getCurrentValue(),0.0,'Current temperature coming less than 0')
		pass
	
	'@Test'
	def testgetAvg(self):
		self.assertGreaterEqual(self.sensor.getAverageValue(),0.0,'Avg coming less than 0')
		pass
	
	'@Test'
	def testgetMin(self):
		self.assertGreaterEqual(self.sensor.getMinValue(),0.0,'Min coming less than 0')
		pass
		
	'@Test'
	def testgetMax(self):
		self.assertGreaterEqual(self.sensor.getMaxValue(),0.0,'Max coming less than 0')
		pass
	
	'@Test'
	def testgetCount(self):
		self.assertGreaterEqual(self.sensor.getCount(),0.0,'sample count coming less than 0')
		pass
		
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()