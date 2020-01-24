import unittest
from labs.module01 import sysMemUtilTask,sysCpuUtilTask
from labs.module01 import SystemPerformanceAdaptor
"""
Test class for all requisite Module01 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class Module01Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
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
	"""
	Testing working of SystemAdapterRun run() method.
	"""
	def testSystemAdapterRun(self):
		self.assertEqual(True,SystemPerformanceAdaptor.run() , "SystemPerformanceAdapter run() not working. The method did not return True")	
	
	"""
	Testing CPU Utilization parameter. Valid parameter should be equal or between 0 and 100
	"""
	def testCpuUtilUpperLimitTest(self):
		#self.assertTrue(100<=sysCpuUtilTask.getDataFromMachine()>=0, )
		self.assertGreaterEqual(100, sysCpuUtilTask.getDataFromMachine(), "CPU utilization should not be greater than 100.")
		
	def testCpuUtilLowerLimitTest(self):
		#self.assertTrue(100<=sysCpuUtilTask.getDataFromMachine()>=0, )
		self.assertGreaterEqual(sysCpuUtilTask.getDataFromMachine(), 0,"CPU utilization should not be less than 0.")	
	
	
	"""
	Testing Memory Utilization parameter. Valid parameter should be equal or between 0 and 100
	"""	
	def testMemUtilUpperLimitTest(self):
		self.assertGreaterEqual(float(100),sysMemUtilTask.getDataFromMachine(), "Memory utilization parameter should not be greater than 100")

	def testMemUtilLowerLimitTest(self):
		self.assertGreaterEqual(sysMemUtilTask.getDataFromMachine(),float(0), "Memory utilization parameter should not be less than 0")

	

		
	
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()