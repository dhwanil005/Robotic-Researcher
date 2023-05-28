import unittest
import sys

sys.path.append('../')
from scientists import Scientist
from robotics import Robot

class ScientistsTest(unittest.TestCase):
    # setting up
    def setUp(self) -> None:
        self.scientist = Scientist("Albert Einstein", "14 March 1879", "18 April 1955", "Albert Einstein was a theoretical physicist.")
    
    # cleaanup
    def tearDown(self) -> None:
        return super().tearDown()
    
    # Success test for scientist name
    def test_scientist_name(self):
        self.assertEqual(self.scientist.get_name(),"Albert Einstein")

    # Success test for scientist birthdate
    def test_birthdate_success(self):
        self.assertEqual(self.scientist.get_birth_date(),"14 March 1879")

    # Success test for Scientist death date
    def test_deathdate_succcess(self):
        self.assertEqual(self.scientist.get_death_date(),"18 April 1955")

    # Success test for introduction
    def test_introduction_success(self):
        self.assertEqual(self.scientist.get_introduction(),"Albert Einstein was a theoretical physicist.")

    # Test to check that calculate_age() method works as it is supposed to
    def test_calculate_age(self):
        self.assertEqual(self.scientist.calculate_age(),76)

    # Fail test for birthdate
    def test_birthdate_failed(self):
        scientist = Scientist("Albert Einstein", None, "18 April 1955", "Albert Einstein was a theoretical physicist.")
        self.assertEqual(scientist.get_birth_date(),"Unavailable")

    # Fail test for deathdate
    def test_deathdate_failed(self):
        scientist = Scientist("Albert Einstein", "14 March 1879", None, "Albert Einstein was a theoretical physicist.")
        self.assertEqual(scientist.get_death_date(),"Unavailable")

    # Fail test for introduction
    def test_introduction_failed(self):
        scientist = Scientist("Albert Einstein", "14 March 1879", "18 April 1955", None)
        self.assertEqual(scientist.get_introduction(),"Unavailable")

    # calculate_age() should return -1 if birth date fails to retrieve
    def test_age_failed_birthdate_error(self):
        scientist = Scientist("Albert Einstein", None, "18 April 1955", "Albert Einstein was a theoretical physicist.")
        self.assertEqual(scientist.calculate_age(),-1)
        
    # calculate_age() should return -1 if death date fails to retrieve
    def test_age_failed_deathdate_error(self):
        scientist = Scientist("Albert Einstein", "14 March 1879", None, "Albert Einstein was a theoretical physicist.")
        self.assertEqual(scientist.calculate_age(),-1)