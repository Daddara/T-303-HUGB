from Classes.appointment import Appointment
from Classes.prescription import Prescription
from Classes.patient import Patient
from Classes.staff import Staff
from data import Data
import json


class Wrapper:
    def __init__(self):
        self.__data = Data()
        self.__patients = self.__data.get_patients()    # return list of dict
        self.__staff = self.__data.get_staff()          #
        self.__appointments = self.__data.get_appointments()
        self.__prescriptions = self.__data.get_prescriptions()
    
    def send_presription (self, data):
        try:
            self.hospital.PharmacyRequests.append([self.pharmecy.get_pharmecy(data[0]), self.patient.get_patient(data[2]), self.medicine.get_medicine(data[4])])
            print("The requests for the pharmecy are now: " + str(self.pharmecy.PharmecyRequests))

            return '{"Order for medicine:' + str(self.pharmecy.PharmecyRequests[0][2][0]) + " to pharmacy: " + str(self.pharmecy.PharmecyRequests[0][0]) +" for patient: " + str(self.pharmecy.PharmecyRequests[0][1][0]) +' }'
        except:
            return '{"Order Failed"}'

    def get_patient_list(self, data):
        return '{"Not implemented"}'

    
    def create_patient(self, data):
        data = json.loads(data)
        try:
            new_patient = Patient(data["ssn"], data["name"], data["address"], data["phone"], data["email"], data["record"])
            print("PATIENT CREATED")
            print(new_patient.get_patient())
            new_patient = new_patient.get_patient()
            return json.dumps(new_patient)
        except:
            return  '{ "No!!!!!" }'