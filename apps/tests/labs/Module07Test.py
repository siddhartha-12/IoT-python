import unittest


"""
Test class for all requisite Module07 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
from labs.module07.CoapClientConnector import CoapClientConnector

class Module07Test(unittest.TestCase):
	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.ccc = CoapClientConnector()
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
	def testSend(self):
		message = "Test"
		self.assertTrue(self.ccc.send(message), "Message issues")
	
	def testPut(self):
		message = "Test"
		self.assertTrue(self.ccc.put(message), "put issues")
	
	def testGet(self):
		message = "Test"
		self.assertTrue(self.ccc.get(), "get issues")	
	
	def testPost(self):
		message = "Test"
		self.assertTrue(self.ccc.put(message), "put issues")
	
	def testDelete(self):
		message = "Test"
		self.assertTrue(self.ccc.delete(), "delete issues")
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()