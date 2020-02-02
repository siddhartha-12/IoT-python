import unittest
from labs.module02.TempSensorEmulatorTask import TempSensorEmulatorTask
from labs.module02.SmtpClientConnector import SmtpClientConnector

"""
Test class for all requisite Module02 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""

class Module02Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.emu = TempSensorEmulatorTask();
		self.smtp = SmtpClientConnector();
		self.config = "../../../config/ConnectedDevicesConfig.props"
		self.tempSensor = TempSensorEmulatorTask();
		pass

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		pass
	
	"""
	Place your comments describing the test here.
	
	def testSomething(self):
		pass
	"""
	'@Test'
	#Testing Lower bound of sensor data
	def testgetData(self):
		self.assertGreaterEqual(self.emu.getSensorData(), 0,"Sensor temp less than 0") 
		pass
	# Testing SMTP connection and test mail 
	def testSmtpData(self):
		self.assertTrue(self.smtp.publishMessage("Python Unit Test check", "If you are receiving this mail then the python smtp test successful"),"Issue in mail server") 
		pass
	# Testing data generation from emulator task
	def testSensorEmulatorTask(self):
		self.assertIsNotNone(self.tempSensor.getSensorData(),"Generated data from getSensordata()") 
		pass
	
	# Testing send notification method
	def testSendNotification(self):
		self.assertIsNotNone(self.tempSensor.sendNotification(),"Generated data from getdata()") 
		pass
	# Testing sensor emulator upper bounds
	def testSensorEmulatorTaskUpperBound(self):
		self.assertGreaterEqual(30,self.tempSensor.getSensorData(),"Generated data from Sensor if greater than 30") 
		pass
	
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()