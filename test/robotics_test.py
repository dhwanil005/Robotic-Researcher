import unittest
import sys
sys.path.append('../')
from robotics import Robot
from scientists import Scientist

class RoboticsTest(unittest.TestCase):
    # setting up
    def setUp(self) -> None:
        self.robot = Robot("Quandrinaut")
        self.webpage = "https://en.wikipedia.org/wiki/Albert_Einstein"
        self.scientist_data = self.robot.fetch_scientist_data(
            self.webpage, "Albert Einstein")
    # Cleanup
    def tearDown(self) -> None:
        self.robot.close_webpage()

    # Tests whether the data is fetched or not
    def test_fetch_scientist_data(self):
        self.assertIsNotNone(self.scientist_data)
        self.assertIsInstance(self.scientist_data, Scientist)
        self.assertEqual(self.scientist_data.get_name(), "Albert Einstein")

    #Success test for birth date
    def test_birthdate_success(self):
        self.assertIsNotNone(self.scientist_data)
        self.assertIsInstance(self.scientist_data, Scientist)
        self.assertEqual(self.scientist_data.get_birth_date(), "14 March 1879")

    #Success test for death date
    def test_deathdate_success(self):
        self.assertIsNotNone(self.scientist_data)
        self.assertIsInstance(self.scientist_data, Scientist)
        self.assertEqual(self.scientist_data.get_death_date(), "18 April 1955")

    #Success test for introduction
    def test_introduction_success(self):
        self.assertIsNotNone(self.scientist_data)
        self.assertIsInstance(self.scientist_data, Scientist)
        self.assertEqual(len(self.scientist_data.get_introduction()), 1103)

    #Fail test for birth date
    def test_birthdate_failed(self):
        webpage = "https://en.wikipedia.org/wiki/abc"
        scientist_data = self.robot.fetch_scientist_data(webpage, "abc")
        self.assertEqual(scientist_data.get_birth_date(), "Unavailable")

    #Fail test for death date
    def test_deathdate_failed(self):
        webpage = "https://en.wikipedia.org/wiki/abc"
        scientist_data = self.robot.fetch_scientist_data(webpage, "abc")
        self.assertEqual(scientist_data.get_death_date(), "Unavailable")

    #Fail test for introduction
    def test_introduction_failed(self):
        webpage = "https://en.wikipedia.org/wiki/adfkgadkf"
        scientist_data = self.robot.fetch_scientist_data(webpage, "adfkgadkf")
        self.assertEqual(scientist_data.get_introduction(), "Unavailable")
    
    # Tests that the open browser method does not throw any exception
    def test_open_browser_throws_no_exception(self):
        try:
            self.robot.fetch_scientist_data(self.webpage, "Albert Einstein")
            "Albert Einstein"
        except Exception as e:
            self.fail(f"An unexpected exception was raised: {e}")
        
            
