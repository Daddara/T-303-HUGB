from appointment import Appointment
from prescription import Prescription
from patient import Patient
from staff import Staff
from doctor import Doctor
from nurse import Nurse


prescriptions_list = [
    Prescription("1", "23", "234")
]

patients_list = [
    Patient("icehot", "Bjarni Benediktsson","icehot@rikid.is", "", "", ""),
    Patient("gudrun1", "Gudrun Hognadottir","gudrun1@gmail.com", '{"Allergies": ["lactose", "nut", "latex"], "Surgeries": ["hip surgery", "brain surgery"]}', "", ""),
    Patient("jonniminn", "Jon Gunnarsson", "jonniminn@tolfan.is", '{"Medication": ["ritalin", "Parkodin", "Astma"]}', "", "")
]

#TODO remove staff list
staff_members = [
    Staff("Johann Johannsson", "1010661399", "doctor", "Hamraborg 20", "8992345"),
    Staff("Gunnar Gunnarsson", "0909691399", "nurse", "Hamraborg 10", "7883456"), 
    Staff("Arna Arnadottir", "0808701399", "specialist", "Hamraborg 30", "5991234"), 
    Staff("Hanna Hannesardottir", "0707891399", "receptionist", "Hamraborg 60", "8566858")]

# username: string, name: string, email: string, note: string, department: string
doctors = [
    Doctor("jojo", "Johann Johannsson", "jojo@gmail.com", "professional hamon user", "surgeon"),
    Doctor("arnaa", "Arna Arnadottir", "arnaa@visir.is", "doctor", "Dermatologist")
]

# username: string, name: string, email: string, note: string
nurses = [
    Nurse("hanna21", "Hanna Hannesardottir", "hanna21@simnet.is", "Great human"),
    Nurse("GunGun", "Gunnar Gunnarsson", "GunGun21@gmail.com", "works slow")
]


appointments = [
    Appointment("icehot", [staff_members[0], staff_members[3]], [10, 8, 2022], "13:00", 60, 2, "Surgery on shoulder"), 
    Appointment("icehot", [staff_members[2]], [12, 9, 2022], "09:00", 30),
    Appointment("icehot", [staff_members[0]], [12, 9, 2022], "19:00", 30)
    ]

class Data():
    ''' Our Database Dummy'''
    def __init__(self):
        pass
    
    def get_doctors(self):
        """Returns a list of doctors created to stand in for our database"""
        return doctors
    
    def get_nurses(self):
        """Returns a list of nurses created to stand in for our database"""
        return nurses

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
        """Returns a list of precriptions made to stand in for our database"""
        return prescriptions_list   
