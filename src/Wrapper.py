import json

from Classes.appointment import Appointment
from Classes.prescription import Prescription
from Classes.patient import Patient
from Classes.staff import Staff
from data import Data

class Wrapper:
    def __init__(self):
        self.__data = Data()
        self.__patients = self.__data.get_patients()  # return list of dict
        self.__staff = self.__data.get_staff()  #
        self.__appointments = self.__data.get_appointments()
        self.__prescriptions = self.__data.get_prescriptions()

    def send_presription(self, data):
        try:
            x = json.loads(data)
            for patient in self.__patients:
                if x["patient_id"] == patient.get_patient_id():
                    newPerscription = Prescription(x["medicine"], x["pharmecy"], x["patient_id"])
                    print(self.__prescriptions)
                    self.__prescriptions.append(newPerscription)
                    print(self.__prescriptions)
                    return_msg = newPerscription.get_return_str()
                    return return_msg
                else:
                    return '{"Not a valid person"}'
        except:
            return '{"Order Failed"}'

    def get_patient_list(self, data):
        self.__patients.get_patient_list(data)
        return '{"Not implemented"}'

    def assign_treatment(self, data):
        return '{"Not implemented"}'
    
    def create_patient(self, data):
        """Takes a json object and turns into a dictionary that is then passed
            to create a Patient object with the data. Returns a json value"""

        data = json.loads(data)
        try:
            new_patient = Patient(data["ssn"], data["name"], data["address"], data["phone"], data["email"], data["record"])
            self.__patients.append(new_patient)
            new_patient = new_patient.get_patient()
            return json.dumps(new_patient)
        except:
            return  '{ "Creating this patient was unsuccessful, please try again." }'
        
    
    def get_patient_info(self, data):
        "Prints out patient if it is listed in the system"
        try:
            x = json.loads(data)
            for patient in self.__patients:
                if patient.get_patient_id() == x["patient_id"]:
                    new_patient = patient.get_patient()
                    return new_patient
        except:
            return '{"No Patient Info"}'

    def delete_patient(self,data):
        
        index = 0
        for dict in self.__patients:
            index +=1
            if( dict[data] == id):
                deleted_patient = self.__patients.pop(dict)
        
        return json.dumps(deleted_patient)
