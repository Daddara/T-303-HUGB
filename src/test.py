# import unittest library - needed to run unit tests
import unittest
# import the proper classes - our test targets ('system under test')
from Classes.prescription import Prescription
from Classes.appointment import Appointment
from Classes.staff import Staff
from Classes.patient import *
from Wrapper import Wrapper
from data import Data

# You have to create a new class inheriting from unittest.TestCase
# All methods in this class will be run by the unittest runner!
class TestStationMethods(unittest.TestCase):
    # set up method - is run before each actual test case.
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
        # all our tests need an instance of WeatherStation, so we just create one here
        self.patient = Patient("0909002020", "Jói Jóason", "Hamraborg 100", "90990909", "joi@gmail.com")
        self.patient_with_allergy = Patient("1212002320", "Gulla Gull", "Hamraborg 200", "8872233", "gulla@hotmail.com", ["Fish allergy", "Nut allergy"])

        self.doctor = Staff("Anna Önnudóttir", "1010661399", "doctor", "Hamraborg 20", "8992345")
        self.nurse = Staff("Gunnar Gunnarsson", "0909691399", "nurse", "Hamraborg 10", "7883456")

        # Þarf ekki að senda inn allar upplýsingar?
        self.appoinment_surgery = Appointment(self.patient, [self.doctor, self.nurse], [10,10,2022], "08:00", 120, 2, "Surgery on shoulder.")
        self.appointment_checkup = Appointment(self.patient, [self.doctor], [10,10,2022], "12:00", 60)

    # This is a single test case - it runs the reportWeather function in our station
    # and makes sure the return value is an empty string
    def test_patient_class(self):
        pass

    def test_staff_class(self):
        pass

    # Eitthvað að reyna að testa
    def test_assign_treatment(self):
        appointment_surgery = self.appoinment_surgery.get_info()
        self.assertIsInstance(appointment_surgery, dict)
        # ekki komnar upplýsingar um patient út af patient klasa
        doctor = appointment_surgery["staff"][0].get_staff_member()
        nurse = appointment_surgery["staff"][1].get_staff_member()
        self.assertEqual(doctor["ssn"], "1010661399")
        self.assertEqual(nurse["ssn"], "0909691399")
        self.assertEqual(appointment_surgery["date"], [10,10,2022])
        self.assertEqual(appointment_surgery["time"], "08:00")
        self.assertEqual(appointment_surgery["duration"], 120)
        self.assertEqual(appointment_surgery["treatment"], "Surgery")
        self.assertEqual(appointment_surgery["description"], "Surgery on shoulder.")

        appointment_checkup = self.appointment_checkup.get_info()
        self.assertIsInstance(appointment_checkup, dict)
        doctor = appointment_checkup["staff"][0].get_staff_member()
        self.assertEqual(doctor["ssn"], "1010661399")
        self.assertEqual(appointment_checkup["date"], [10,10,2022])
        self.assertEqual(appointment_checkup["time"], "12:00")
        self.assertEqual(appointment_checkup["duration"], 60)
        self.assertEqual(appointment_checkup["treatment"], "Checkup")
        self.assertEqual(appointment_checkup["description"], "")

    def test_wrapper(self):
        pass

    # tear down method - is run after each test case
    def tearDown(self):
        print("Test done.")


# If this file is run with python, it will just execute all tests within this file
if __name__ == "__main__":
    unittest.main()