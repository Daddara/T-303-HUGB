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
            newPerscription = Prescription(data[0], data[1], data[2])
            print(self.__prescriptions)
            self.__prescriptions.append(newPerscription)
            print(self.__prescriptions)
            return_msg = newPerscription.get_return_str()
            return return_msg

        except:
            return '{"Order Failed"}'

    def get_patient_list(self, data):
        return '{"Not implemented"}'