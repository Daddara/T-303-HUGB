# import unittest library - needed to run unit tests
import unittest

# import the WeatherStation class - our test target ('system under test')
from Classes.patient import Patient
from Classes.appointment import Appointment

# You have to create a new class inheriting from unittest.TestCase
# All methods in this class will be run by the unittest runner!
class TestStationMethods(unittest.TestCase):
    # set up method - is run before each actual test case.
    def setUp(self):
        # all our tests need an instance of WeatherStation, so we just create one here
        self.patient = Patient()

        # Þarf ekki að senda inn allar upplýsingar?
        self.appoinment = Appointment()

    # This is a single test case - it runs the reportWeather function in our station
    # and makes sure the return value is an empty string
    def test_patient_name(self):
        # Run function
        patient_record = self.patient.get_patient("1")

        # Assertion
        self.assertEqual(patient_record[0], "Sara")
        self.assertNotEqual(patient_record[1], "21")

    def test_report_status(self):
        #     #Run function
        status = ""  # self.my_station.report_status()

        # Assertion
        self.assertEqual("", status)

    # Eitthvað að reyna að testa
    def test_assign_treatment(self):
        appointment = self.appoinment.get_info()

        self.assertEqual(appointment[0], "Einhver patient")

    # tear down method - is run after each test case
    def tearDown(self):
        print("Test done.")


# If this file is run with python, it will just execute all tests within this file
if __name__ == "__main__":
    unittest.main()