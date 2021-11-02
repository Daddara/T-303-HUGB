from data import Data
import json
from Classes.prescription import Prescription

class PrescriptionLogic():
    def __init__(self):
        self.__data = Data()
        self.__prescriptions = self.__data.get_prescriptions()
    
    def get_prescription_database(self):
        return self.__prescriptions
    
    def send_presription(self, data, patient_list):
        ''' This function takes in name of medicine and pharmecy along with the id of a patient.
        The function uses it to send a prescription for the medicine to the pharmecy for the patient. 
        As of now, you can only prescribe existing patients with Ibufen or Parcodine, at either 
        the Apótekið or Heilsuver'''
        try:
            theData = json.loads(data)
            for patient in patient_list:
                if theData["patient_id"] == patient.get_patient_id():
                    if theData["medicine"] == "Ibufen" or theData["medicine"] == "Parkodín":
                        if theData["pharmecy"] == "Apótekið" or theData["pharmecy"] == "Heilsuver":
                            newPrescription = Prescription(theData["medicine"], theData["pharmecy"], theData["patient_id"])
                            self.__prescriptions.append(newPrescription)
                            return_msg = newPrescription.get_return_str()
                            return return_msg
                        else:
                            return '{"msg": "Not a valid pharmecy"}'
                    else: 
                        return '{"msg": "Not a valid medicine"}'
            else:
                return '{"msg": "Not a valid person"}'
        except:
            return '{"msg": "Order Failed"}'