#import unittest library - needed to run unit tests
import unittest
#import the WeatherStation class - our test target ('system under test')
from Classes.prescription import *
from Classes.appointment import *
from Classes.staff import *
from Classes.patient import *
from Wrapper import Wrapper
from data import Data


#You have to create a new class inheriting from unittest.TestCase
#All methods in this class will be run by the unittest runner!
class TestStationMethods(unittest.TestCase):
    #set up method - is run before each actual test case.
    def setUp(self):
        #all our tests need an instance of WeatherStation, so we just create one here

        # self.patient = Patient()
        self.prescription = Prescription("Ibufen", "Heilsa", "190500-2330")
        # self.appointment = Appointment()
        # self.staff = Staff()


    def test_prescription_class(self):

        self.assertEqual(self.prescription.get_patient_id(),"190500-2330")
        self.assertEqual(self.prescription.get_pharmecy_name(), "Heilsa")
        self.assertEqual(self.prescription.get_medicine_name(), "Ibufen")
        self.assertEqual(self.prescription.get_return_str(), '{"medicine": "Ibufen", "pharmecy": "Heilsa", "patient_id": "190500-2330"}')

    def test_Wrapper_send_prescription(self):
        wrapper = Wrapper()

        return_msg = wrapper.send_presription('{"medicine": "Daniel", "pharmecy": "Sara", "patient_id": "Sigur"}')

        self.assertEqual(return_msg, '{"medicine": "Daniel", "pharmecy": "Sara", "patient_id": "Sigur"}')

    # #This is a single test case - it runs the reportWeather function in our station
    # #and makes sure the return value is an empty string
    # def test_patient_name(self):
    #     #Run function
    #     patient_record = self.patient.get_patient("1")

    #     #Assertion
    #     self.assertEqual(patient_record[0],"Sara")
    #     self.assertNotEqual(patient_record[1], "21")

    # def test_report_status (self):
    # #     #Run function
    #     status = ""#self.my_station.report_status()

    #     #Assertion
    #     self.assertEqual("",status)

    #tear down method - is run after each test case
    def tearDown(self):
        print("Test done.")

#If this file is run with python, it will just execute all tests within this file
if __name__ == '__main__':
    unittest.main()