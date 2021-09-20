from Classes.appointment import Appointment
from Classes.prescription import Prescription
from Classes.patient import Patient
from Classes.staff import Staff


patients_list = [
    Patient("")
]


class Data():
    ''' Our Database Dummy'''
    def __init__(self):
        pass

    def get_patients(self):
        return []

    def get_appointments(self):
        return []

    def get_staff(self):
        return []

    def get_prescriptions(self):
        return []
    