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

        self.prescription = Prescription("Ibufen", "Heilsa", "190500-2330")

        self.patient = Patient("icehot", "Bjarni Benediktsson","icehot@rikid.is", "", "", "")
        self.patient_with_allergy = Patient("gudrun1", "Gudrun Hognadottir","gudrun1@gmail.com", '{"Allergies": ["lactose", "nut", "latex"], "Surgeries": ["hip surgery", "brain surgery"]}', "", "")

        self.doctor = Staff("Anna Önnudóttir", "1010661399", "doctor", "Hamraborg 20", "8992345")
        self.nurse = Staff("Gunnar Gunnarsson", "0909691399", "nurse", "Hamraborg 10", "7883456")

        self.appoinment_surgery = Appointment("icehot", [self.doctor, self.nurse], [10,10,2022], "08:00", 120, 2, "Surgery on shoulder.")
        self.appointment_checkup = Appointment("gudrun1", [self.doctor], [10,10,2022], "12:00", 60)

    def test_wrapper(self):
        wrapper = Wrapper()

        # delete staff member
        self.assertEqual(wrapper.delete_staff_member('{"staff_ssn": "0808701399"}'), '{"name": "Arna Arnadottir", "ssn": "0808701399", "address": "Hamraborg 30", "phone": "5991234", "title": "specialist"}')
        self.assertEqual(wrapper.delete_staff_member('{"staff_ssn": "2202002020"}'), '{"msg":"No staff member with this ssn"}')


    def test_prescription_class(self):
        # First one needs to be change due to the difference in the patient class
        # self.assertEqual(self.prescription.get_patient_id(),"")
        self.assertEqual(self.prescription.get_pharmecy_name(), "Heilsa")
        self.assertEqual(self.prescription.get_medicine_name(), "Ibufen")
        self.assertEqual(self.prescription.get_return_str(), '{"medicine": "Ibufen", "pharmecy": "Heilsa", "patient_id": "190500-2330"}')

    def test_patient_class(self):
        """Testing wether the patient class works correctly"""
        patient_one = self.patient.get_patient()
        patient_two = self.patient_with_allergy.get_patient()
        self.assertIsInstance(self.patient, Patient)
        self.assertIsInstance(self.patient_with_allergy, Patient)
        self.assertIsInstance(patient_one, dict)
        self.assertIsInstance(patient_two, dict)

        self.assertEqual(patient_one["username"], "icehot")
        self.assertEqual(patient_one["name"], "Bjarni Benediktsson")
        self.assertEqual(patient_one["email"], "icehot@rikid.is")
        self.assertEqual(patient_one["note"], "")
        self.assertEqual(patient_one["doctorid"], "")
        self.assertEqual(patient_one["nurseid"], "")

        self.assertEqual(patient_two["username"], "gudrun1")
        self.assertEqual(patient_two["name"], "Gudrun Hognadottir")
        self.assertEqual(patient_two["email"], "gudrun1@gmail.com")
        self.assertEqual(patient_two["note"], '{"Allergies": ["lactose", "nut", "latex"], "Surgeries": ["hip surgery", "brain surgery"]}')
        self.assertEqual(patient_two["doctorid"], "")
        self.assertEqual(patient_two["nurseid"], "")



    def test_staff_class(self):
        """Testing wether the staff class works correctly"""
        doctor = self.doctor.get_staff_member()
        nurse = self.nurse.get_staff_member()
        self.assertIsInstance(self.doctor, Staff)
        self.assertIsInstance(self.nurse, Staff)
        self.assertIsInstance(doctor, dict)
        self.assertIsInstance(nurse, dict)

        self.assertEqual(doctor["ssn"], "1010661399")
        self.assertEqual(doctor["name"], "Anna Önnudóttir")
        self.assertEqual(doctor["title"], "doctor")
        self.assertEqual(doctor["address"], "Hamraborg 20")
        self.assertEqual(doctor["phone"], "8992345")

        self.assertEqual(nurse["ssn"], "0909691399")
        self.assertEqual(nurse["name"], "Gunnar Gunnarsson")
        self.assertEqual(nurse["title"], "nurse")
        self.assertEqual(nurse["address"], "Hamraborg 10")
        self.assertEqual(nurse["phone"],"7883456")


    def test_appointment_class(self):
        """Testing wether the appointment class works correctly"""
        appointment_surgery = self.appoinment_surgery.get_info()
        self.assertIsInstance(appointment_surgery, dict)
        self.assertIsInstance(appointment_surgery["patient"], str)
        self.assertEqual(appointment_surgery["patient"], "icehot")
        doctor = appointment_surgery["staff"][0].get_staff_member()
        nurse = appointment_surgery["staff"][1].get_staff_member()
        self.assertEqual(len(appointment_surgery["staff"]), 2)
        self.assertEqual(doctor["ssn"], "1010661399")
        self.assertEqual(nurse["ssn"], "0909691399")
        self.assertEqual(appointment_surgery["date"], [10,10,2022])
        self.assertEqual(appointment_surgery["time"], "08:00")
        self.assertEqual(appointment_surgery["duration"], 120)
        self.assertEqual(appointment_surgery["treatment"], "Surgery")
        self.assertEqual(appointment_surgery["description"], "Surgery on shoulder.")

        appointment_checkup = self.appointment_checkup.get_info()
        self.assertIsInstance(appointment_checkup, dict)
        self.assertIsInstance(appointment_checkup["patient"], str)
        self.assertEqual(appointment_checkup["patient"], "gudrun1")
        doctor = appointment_checkup["staff"][0].get_staff_member()
        self.assertEqual(len(appointment_checkup["staff"]), 1)
        self.assertEqual(doctor["ssn"], "1010661399")
        self.assertEqual(appointment_checkup["date"], [10,10,2022])
        self.assertEqual(appointment_checkup["time"], "12:00")
        self.assertEqual(appointment_checkup["duration"], 60)
        self.assertEqual(appointment_checkup["treatment"], "Checkup")
        self.assertEqual(appointment_checkup["description"], "")
        self.assertEqual(self.appointment_checkup.check_appointments("1010661399"), True)
        self.assertEqual(self.appointment_checkup.check_appointments("2202002020"), False)


    # tear down method - is run after each test case
    def tearDown(self):
        print("Test done.")


# If this file is run with python, it will just execute all tests within this file
if __name__ == "__main__":
    unittest.main()
