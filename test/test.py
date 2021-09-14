#import unittest library - needed to run unit tests
import unittest

#import the WeatherStation class - our test target ('system under test')
from src.HospitalSystem_if import Patients

#You have to create a new class inheriting from unittest.TestCase
#All methods in this class will be run by the unittest runner!
class TestStationMethods(unittest.TestCase):
    #set up method - is run before each actual test case.
    def setUp(self):
        #all our tests need an instance of WeatherStation, so we just create one here
        self.patient = Patients("Bubbi Morthens")

    #This is a single test case - it runs the reportWeather function in our station
    #and makes sure the return value is an empty string
    def test_patient_name(self):
        #Run function
        patient_record = self.patient.get-patient()

        #Assertion
        self.assertEqual("",patient_record)
        self.assertEqual(1,1)

    # def test_report_status (self):
    #     #Run function
    #     status = self.my_station.report_status()

    #     #Assertion
    #     self.assertEqual("",status)

    #tear down method - is run after each test case
    def tearDown(self):
        print("Test done.")

#If this file is run with python, it will just execute all tests within this file
if __name__ == '__main__':
    unittest.main()