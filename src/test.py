# import unittest library - needed to run unit tests
import unittest

import websockets
# import the proper classes - our test targets ('system under test')
from Classes.prescription import Prescription
from Classes.appointment import Appointment
from Classes.staff import Staff
from Classes.patient import Patient
from Classes.doctor import Doctor
from Classes.nurse import Nurse
from Wrapper import Wrapper
from data import Data
import json

# You have to create a new class inheriting from unittest.TestCase
# All methods in this class will be run by the unittest runner!
class TestStationMethods(unittest.TestCase):
    # set up method - is run before each actual test case.
    def setUp(self):

        self.prescription = Prescription("Ibufen", "Heilsa", "190500-2330")

        self.patient = Patient("icehot", "Bjarni Benediktsson","icehot@rikid.is", "", "", "")
        self.patient_with_allergy = Patient("gudrun1", "Gudrun Hognadottir","gudrun1@gmail.com", '{"Allergies": ["lactose", "nut", "latex"], "Surgeries": ["hip surgery", "brain surgery"]}', "", "")

        self.staff1 = Staff("Anna Önnudóttir", "1010661399", "doctor", "Hamraborg 20", "8992345")
        self.staff2 = Staff("Gunnar Gunnarsson", "0909691399", "nurse", "Hamraborg 10", "7883456")

        self.doctor1 = Doctor("jojo", "Johann Johannsson", "jojo@gmail.com", "professional hamon user", "surgeon")
        self.doctor2 = Doctor("arnaa", "Arna Arnadottir", "arnaa@visir.is", "doctor", "Dermatologist")

        self.nurse1 = Nurse("hanna21", "Hanna Hannesardottir", "hanna21@simnet.is", "Great human")
        self.nurse2 = Nurse("GunGun", "Gunnar Gunnarsson", "GunGun21@gmail.com", "works slow")

        self.appoinment_surgery = Appointment("icehot", ["jojo"], [10,10,2022], "08:00", 120, 2, "Surgery on shoulder.")
        self.appointment_checkup = Appointment("gudrun1", ["arnaa"], [10,10,2022], "12:00", 60)

    def test_wrapper(self):
        wrapper = Wrapper()

        # delete staff member
        self.assertEqual(wrapper.delete_staff_member('{"staff_ssn": "0808701399"}'), '{"name": "Arna Arnadottir", "ssn": "0808701399", "address": "Hamraborg 30", "phone": "5991234", "title": "specialist"}')
        self.assertEqual(wrapper.delete_staff_member('{"staff_ssn": "2202002020"}'), '{"msg":"No staff member with this ssn"}')
        
        # get appointments for arnaa
        self.assertEqual(wrapper.get_appointments('{"username": "arnaa"}'), '{"msg": [{"patient": "icehot", "staff": ["arnaa"], "date": [10, 8, 2022], "time": "13:00", "duration": 60, "treatment": "Surgery", "description": "Surgery on shoulder"}, {"patient": "icehot", "staff": ["arnaa"], "date": [12, 9, 2022], "time": "09:00", "duration": 30, "treatment": "Checkup", "description": ""}, {"patient": "icehot", "staff": ["arnaa"], "date": [12, 9, 2022], "time": "19:00", "duration": 30, "treatment": "Checkup", "description": ""}]}')

        # get appointments for Doctor jojo from 2.2.2020 - 28.2.2020 and 3.2.2020 - 4.2.2020
        self.assertEqual(wrapper.get_appointments_at_date('{"doctor": "jojo", "from_date" : ["2","2","2020"], "to_date":["28","2","2020"]}'), '{"msg": [{"patient": "gudrun1", "staff": ["jojo"], "date": [2, 2, 2020], "time": "8:00", "duration": 60, "treatment": "Checkup", "description": ""}]}')
        self.assertEqual(wrapper.get_appointments_at_date('{"doctor": "jojo", "from_date" : ["3","2","2020"], "to_date":["4","2","2020"]}'), '{"msg":"No appointments"}')

        # Create a receipt for icehot recieving surgery
        self.assertEqual(wrapper.charge_for_service('{"patient":"icehot", "treatment":"2", "reason":"", "price":""}'), '{"msg": {"patient": "icehot", "text": "Surgery", "price": 50000}}')

        # Delete Nurse
        self.assertEqual(wrapper.delete_nurse({"username":"Babba"}), '{"msg": "There is no nurse with this username"}')
        self.assertEqual(wrapper.delete_nurse({"username":"hanna21"}), '{"username": "hanna21", "name": "Hanna Hannesardottir", "email": "hanna21@simnet.is", "note": "Great human"}')

        # Delete Doctor
        self.assertEqual(wrapper.delete_doctor({"username": "SaraH"}), '{"msg": "There is no doctor with this username"}')
        self.assertEqual(wrapper.delete_doctor({"username": "jojo"}), '{"username": "jojo", "name": "Johann Johannsson", "email": "jojo@gmail.com", "note": "professional hamon user", "department": "surgeon"}')


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
        self.assertEqual(patient_one["doctor_id"], "")
        self.assertEqual(patient_one["nurseid"], "")
        self.assertEqual(self.patient.get_patient_name(), patient_one["name"])
        self.assertEqual(self.patient.get_patient_records(), patient_one["note"])
        self.assertEqual(self.patient.get_patient_id(), patient_one["username"])
        self.assertEqual(self.patient.get_patient_email(), patient_one["email"])

        self.assertEqual(patient_two["username"], "gudrun1")
        self.assertEqual(patient_two["name"], "Gudrun Hognadottir")
        self.assertEqual(patient_two["email"], "gudrun1@gmail.com")
        self.assertEqual(patient_two["note"], '{"Allergies": ["lactose", "nut", "latex"], "Surgeries": ["hip surgery", "brain surgery"]}')
        self.assertEqual(patient_two["doctor_id"], "")
        self.assertEqual(patient_two["nurseid"], "")
        self.assertEqual(self.patient_with_allergy.get_patient_name(), patient_two["name"])
        self.assertEqual(self.patient_with_allergy.get_patient_records(), patient_two["note"])
        self.assertEqual(self.patient_with_allergy.get_patient_id(), patient_two["username"])
        self.assertEqual(self.patient_with_allergy.get_patient_email(), patient_two["email"])



    def test_staff_class(self):
        """Testing wether the staff class works correctly"""
        staff1 = self.staff1.get_staff_member()
        staff2 = self.staff2.get_staff_member()
        self.assertIsInstance(self.staff1, Staff)
        self.assertIsInstance(self.staff2, Staff)
        self.assertIsInstance(staff1, dict)
        self.assertIsInstance(staff2, dict)

        self.assertEqual(staff1["ssn"], "1010661399")
        self.assertEqual(staff1["name"], "Anna Önnudóttir")
        self.assertEqual(staff1["title"], "doctor")
        self.assertEqual(staff1["address"], "Hamraborg 20")
        self.assertEqual(staff1["phone"], "8992345")

        self.assertEqual(staff2["ssn"], "0909691399")
        self.assertEqual(staff2["name"], "Gunnar Gunnarsson")
        self.assertEqual(staff2["title"], "nurse")
        self.assertEqual(staff2["address"], "Hamraborg 10")
        self.assertEqual(staff2["phone"],"7883456")

    def test_doctor_class(self):
        doctor1 = self.doctor1.get_info()
        doctor2 = self.doctor2.get_info()
        self.assertIsInstance(self.doctor1, Doctor)
        self.assertIsInstance(self.doctor2, Doctor)
        self.assertEqual(doctor1["username"], self.doctor1.get_username())
        self.assertEqual(doctor2["username"], self.doctor2.get_username())
        self.assertEqual(doctor1["email"], self.doctor1.get_doctor_email())
        self.assertEqual(doctor2["email"], self.doctor2.get_doctor_email())



    def test_nurse_cless(self):
        nurse1 = self.nurse1.get_info()
        nurse2 = self.nurse2.get_info()
        self.assertIsInstance(self.nurse1, Nurse)
        self.assertIsInstance(self.nurse2, Nurse)
        self.assertEqual(nurse1["username"], self.nurse1.get_username())
        self.assertEqual(nurse2["username"], self.nurse2.get_username())
        self.assertEqual(nurse1["email"], self.nurse1.get_nurse_email())
        self.assertEqual(nurse2["email"], self.nurse2.get_nurse_email())

    def test_appointment_class(self):
        """Testing wether the appointment class works correctly"""
        appointment_surgery = self.appoinment_surgery.get_info()
        self.assertIsInstance(appointment_surgery, dict)
        self.assertIsInstance(appointment_surgery["patient"], str)
        self.assertEqual(appointment_surgery["patient"], "icehot")
        self.assertEqual(appointment_surgery["staff"][0], "jojo")
        self.assertEqual(len(appointment_surgery["staff"]), 1)
        self.assertEqual(appointment_surgery["date"], [10,10,2022])
        self.assertEqual(appointment_surgery["date"], self.appoinment_surgery.get_date())
        self.assertEqual(appointment_surgery["time"], "08:00")
        self.assertEqual(appointment_surgery["duration"], 120)
        self.assertEqual(appointment_surgery["treatment"], "Surgery")
        self.assertEqual(appointment_surgery["description"], "Surgery on shoulder.")
        self.assertEqual(self.appoinment_surgery.check_doctor("arnaa"), False)
        self.assertEqual(self.appoinment_surgery.check_doctor("jojo"), True)

        appointment_checkup = self.appointment_checkup.get_info()
        self.assertIsInstance(appointment_checkup, dict)
        self.assertIsInstance(appointment_checkup["patient"], str)
        self.assertEqual(appointment_checkup["patient"], "gudrun1")
        self.assertEqual(appointment_checkup["staff"][0], "arnaa")
        self.assertEqual(len(appointment_checkup["staff"]), 1)
        self.assertEqual(appointment_checkup["date"], [10,10,2022])
        self.assertEqual(appointment_checkup["date"], self.appointment_checkup.get_date())
        self.assertEqual(appointment_checkup["time"], "12:00")
        self.assertEqual(appointment_checkup["duration"], 60)
        self.assertEqual(appointment_checkup["treatment"], "Checkup")
        self.assertEqual(appointment_checkup["description"], "")
        self.assertEqual(self.appointment_checkup.check_doctor("arnaa"), True)
        self.assertEqual(self.appointment_checkup.check_doctor("jojo"), False)
    

    # tear down method - is run after each test case
    def tearDown(self):
        print("Test done.")


# If this file is run with python, it will just execute all tests within this file
if __name__ == "__main__":
    unittest.main()
