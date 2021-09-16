from Classes import *
from Classes.Patients import *
from Classes.Medicine import *
from Classes.Pharmecy import *

class Wrapper:
    def __init__(self):
        self.patients = Patients()
        self.medicine = Medicine()
        self.pharmecy = Pharmecy()
    
    def send_presription (self, data):
        try:
            PharmecyRequests.append([self.pharmecy.get_pharmecy(data[0]), self.patient.get_patient(data[2]), self.medicine.get_medicine(data[4])])
            print("The requests for the pharmecy are now: " + str(PharmecyRequests))

            return '{"Order for medicine:' + str(PharmecyRequests[0][2][0]) + " to pharmacy: " + str(PharmecyRequests[0][0]) +" for patient: " + str(PharmecyRequests[0][1][0]) +' }'
        except:
            return '{"Order Failed"}'