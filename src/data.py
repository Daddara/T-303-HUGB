from Classes.appointment import Appointment
from Classes.prescription import Prescription
from Classes.patient import Patient
from Classes.staff import Staff


patients_list = [
    Patient("Sara" , "270590-2999", "Dufnaholar", "555-5555", "sara@ru.is"),
    Patient("Daniel", "160580-3889", "Menntavegur", "555-44444", "daniel@ru.is")
]


class Data():
    ''' Our Database Dummy'''
    def __init__(self):
        pass

    def get_patients(self):
        return patients_list

    def get_appointments(self):
        return []

    def get_staff(self):
        return []

    def get_prescriptions(self):
        return []    
    