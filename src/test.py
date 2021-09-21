# import unittest library - needed to run unit tests
import unittest

# import the proper classes - our test targets ('system under test')
from Classes.patient import Patient
from Classes.staff import Staff
from Classes.appointment import Appointment

# You have to create a new class inheriting from unittest.TestCase
# All methods in this class will be run by the unittest runner!
class TestStationMethods(unittest.TestCase):
    # set up method - is run before each actual test case.
    def setUp(self):
        # all our tests need an instance of WeatherStation, so we just create one here
        self.patient = Patient("0909002020", "Jói Jóason", "Hamraborg 100", "90990909", "joi@gmail.com")
        self.patient_with_allergy = Patient("1212002320", "Gulla Gull", "Hamraborg 200", "8872233", "gulla@hotmail.com", ["Fish allergy", "Nut allergy"])

        self.doctor = Staff("Anna Önnudóttir", "1010661399", "doctor", "Hamraborg 20", "8992345")
        self.nurse = Staff("Gunnar Gunnarsson", "0909691399", "nurse", "Hamraborg 10", "7883456")

        self.appoinment_surgery = Appointment(self.patient, [self.doctor, self.nurse], [10,10,2022], "08:00", 120, 2, "Surgery on shoulder.")
        self.appointment_checkup = Appointment(self.patient, [self.doctor], [10,10,2022], "12:00", 60)

    # This is a single test case - it runs the reportWeather function in our station
    # and makes sure the return value is an empty string
    def test_patient_class(self):
        """Testing wether the patient class works correctly"""
        patient_one = self.patient.get_patient()
        patient_two = self.patient_with_allergy.get_patient()
        self.assertIsInstance(self.patient, Patient)
        self.assertIsInstance(self.patient_with_allergy, Patient)
        self.assertIsInstance(patient_one, dict)
        self.assertIsInstance(patient_two, dict)

        self.assertEquals(patient_one["ssn"], "0909002020")
        self.assertEquals(patient_one["name"], "Jói Jóason")
        self.assertEquals(patient_one["address"], "Hamraborg 100")
        self.assertEquals(patient_one["phone"], "90990909")
        self.assertEquals(patient_one["email"], "joi@gmail.com")
        self.assertIsInstance(patient_one["record"], list)
        self.assertEquals(len(patient_one["record"]), 0)

        self.assertEquals(patient_two["ssn"], "1212002320")
        self.assertEquals(patient_two["name"], "Gulla Gull")
        self.assertEquals(patient_two["address"], "Hamraborg 200")
        self.assertEquals(patient_two["phone"], "8872233")
        self.assertEquals(patient_two["email"], "gulla@hotmail.com")
        self.assertIsInstance(patient_two["record"], list)
        self.assertEquals(len(patient_two["record"]), 2)


    def test_staff_class(self):
        """Testing wether the staff class works correctly"""
        doctor = self.doctor.get_staff_member()
        nurse = self.nurse.get_staff_member()
        self.assertIsInstance(self.doctor, Staff)
        self.assertIsInstance(self.nurse, Staff)
        self.assertIsInstance(doctor, dict)
        self.assertIsInstance(nurse, dict)

        self.assertEquals(doctor["ssn"], "1010661399")
        self.assertEquals(doctor["name"], "Anna Önnudóttir")
        self.assertEquals(doctor["title"], "doctor")
        self.assertEquals(doctor["address"], "Hamraborg 20")
        self.assertEquals(doctor["phone"], "8992345")

        self.assertEquals(nurse["ssn"], "0909691399")
        self.assertEquals(nurse["name"], "Gunnar Gunnarsson")
        self.assertEquals(nurse["title"], "nurse")
        self.assertEquals(nurse["address"], "Hamraborg 10")
        self.assertEquals(nurse["phone"],"7883456")


    def test_appointment_class(self):
        """Testing wether the appointment class works correctly"""
        appointment_surgery = self.appoinment_surgery.get_info()
        self.assertIsInstance(appointment_surgery, dict)
        # ekki komnar upplýsingar um patient út af patient klasa
        doctor = appointment_surgery["staff"][0].get_staff_member()
        nurse = appointment_surgery["staff"][1].get_staff_member()
        self.assertEquals(len(appointment_surgery["staff"]), 2)
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
        self.assertEquals(len(appointment_checkup["staff"]), 1)
        self.assertEqual(doctor["ssn"], "1010661399")
        self.assertEqual(appointment_checkup["date"], [10,10,2022])
        self.assertEqual(appointment_checkup["time"], "12:00")
        self.assertEqual(appointment_checkup["duration"], 60)
        self.assertEqual(appointment_checkup["treatment"], "Checkup")
        self.assertEqual(appointment_checkup["description"], "")

    def test_prescription_class(self):
        pass

    def test_wrapper(self):
        pass

    # tear down method - is run after each test case
    def tearDown(self):
        print("Test done.")


# If this file is run with python, it will just execute all tests within this file
if __name__ == "__main__":
    unittest.main()