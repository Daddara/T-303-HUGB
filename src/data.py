from Classes.appointment import Appointment
from Classes.prescription import Prescription
from Classes.patient import Patient
from Classes.staff import Staff


patients_list = [
    Patient("")
]

staff_members = [Staff("Jóhann Jóhannsson", "1010661399", "doctor", "Hamraborg 20", "8992345"), Staff("Gunnar Gunnarsson", "0909691399", "nurse", "Hamraborg 10", "7883456"), Staff("Arna Árnadóttir", "0808701399", "specialist", "Hamraborg 30", "5991234"), Staff("Hanna Hannesardóttir", "0707891399", "receptionist", "Hamraborg 60", "8566858")]

appointments = [Appointment(patients_list[0], [staff_members[0], staff_members[2]], [10, 8, 2022], "13:00", 60, 2, "Surgery on shoulder"), Appointment(patients_list[0], [staff_members[2]], [12, 9, 2022], "09:00", 30)]

class Data():
    ''' Our Database Dummy'''
    def __init__(self):
        pass

    def get_patients(self):
        return []

    def get_appointments(self):
        return appointments

    def get_staff(self):
        return []

    def get_prescriptions(self):
        return []
    