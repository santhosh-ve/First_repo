import unittest

def setUpModule():
    print("First_Module")
def tearDownModule():
    print("Last_Module")

class WebTest(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:    #Execute before each test method
        print("login_method")
    def tearDown(self) -> None: #Execute after each test method
        print("logout_method")
    
	@classmethod
    def setUpClass(cls) -> None:    #Execute once the class is started
        print("Open_Class")
    @classmethod
    def tearDownClass(cls) -> None: #Execute once after the class methods completed
        print("Close_Class")
	
	#Test methods	
    def test_search(self):
        print("Search")
	@unittest.SkipTest			#To skip a test
	@unittest.skip("Reason")
	@unittest.skipIf()
    def test_advsearch(self):
        print("Advanced")
    def test_prepaid(self):
        print("Preparid")
    def test_postpaid(self):
        print("Postpaid")

#Calling the tests
if __name__=="__main__":
    unittest.main()

#assertions
assertEqual()
assertNotEqual()
assertTrue()
assertFalse()
assertIn()
assertNotIn()
assertIsNone()
assertIsNotNone()
assertGreater()
assertGreaterEqual()
assertLess()
assertLessEqual()

#TestSuites and TestCases

-->Create testcases in different packages
	Package1
		Testcase1
		Testcase2
	Package2
		Testcase3
		Testcase4
-->Create a package which holds TestSuite
	Package3
		Testsuite
-->import the packages and testcases

-->To get the test methods from testcases
	Testcase = unittest.TestLoader().loadTestFromTestCase(classname)
	
-->To create testsuite
	TestSuiteName = unittest.TestSuite([Testcase])
	unittest.TextTestRunner().run(TestSuiteName)

