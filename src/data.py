from Classes.appointment import Appointment
from Classes.prescription import Prescription
from Classes.patient import Patient
from Classes.staff import Staff


prescriptions_list = [
    Prescription("1", "23", "234")
]

patients_list = [
    Patient("1212889909", "Bjarni Benediktsson", "Akurbraut 17, 200", 8887122, "icehot@rikid.is", {}),
    Patient("3110659989", "Gudrun Hognadottir", "Hvervisgata 30, 101", 6671129, "gudrun1@gmail.com", {"Allergies": ["lactose", "nut", "latex"], "Surgeries": ["hip surgery", "brain surgery"]}),
    Patient("0101059980", "Jon Gunnarsson", "Hamraborg 19, 201", 9910345, "jonniminn@tolfan.is", {"Medication": ["ritalin", "Parkodin", "Astma"]})
]

staff_members = [
    Staff("Johann Johannsson", "1010661399", "doctor", "Hamraborg 20", "8992345"),
    Staff("Gunnar Gunnarsson", "0909691399", "nurse", "Hamraborg 10", "7883456"), 
    Staff("Arna Arnadottir", "0808701399", "specialist", "Hamraborg 30", "5991234"), 
    Staff("Hanna Hannesardottir", "0707891399", "receptionist", "Hamraborg 60", "8566858")]

appointments = [
    Appointment(patients_list[0], [staff_members[0], staff_members[2]], [10, 8, 2022], "13:00", 60, 2, "Surgery on shoulder"), 
    Appointment(patients_list[0], [staff_members[2]], [12, 9, 2022], "09:00", 30),
    Appointment(patients_list[0], [staff_members[0]], [12, 9, 2022], "19:00", 30)
    ]
    


class Data():
    ''' Our Database Dummy'''
    def __init__(self):
        pass

    def get_patients(self):
        """Returns a list of patients created to stand in for our database"""
        return patients_list

    def get_appointments(self):
        """Returns a list of appointments created to stand in for our database"""
        return appointments

    def get_staff(self):
        """Returns a list of staff members created to stand in for our database"""
        return staff_members

    def get_prescriptions(self):
        return prescriptions_list   
