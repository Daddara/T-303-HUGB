from data import Data
import json
from Classes.patient import Patient

class PatientLogic():
    """contains all Logic and Dummydata for paatients"""
    def __init__(self):
        self.__data = Data()
        self.__patients = self.__data.get_patients()
    
    def get_patient_database(self):
        """returns list of all patients from the database"""
        return self.__patients

    def update_patient(self, data):
        """Updates information about an existing patient."""
        try:
            if "username" in data:
                message = {}
                emails = []
                for patient in self.__patients: #This forloop is to get all existing emails to make sure that the emails are not repeated.
                    emails.append(patient.get_patient_id())
                for patient in self.__patients:
                    username = data["username"]
                    if patient.get_patient_id() == username:
                        if "@" in data["email"]:
                            new_username = data["email"].split("@")
                            if new_username[1] != '':
                                emails.remove(patient.get_patient_id())
                                if new_username[0] not in emails:
                                    updated_patient = patient.update_patient(new_username[0], data["name"], data["email"], data["note"], data["doctor_id"])
                                else:
                                    updated_patient = patient.update_patient(patient.get_patient_id(), data["name"], patient.get_patient_email(), data["note"], data["doctor_id"])
                        json.dumps(message)
                message["msg"] = updated_patient
                return json.dumps(message)

            else:
                return '{"msg": "username needed!"}'
        except:
            return  '{ "msg": "Updating this patient was unsuccessful, please try again." }'

    def get_patient_list(self):
        """Returns all patients' info as dictionaries"""
        message = {}
        pat_list = []
        for patient in self.__patients:
            pat_list.append(patient.get_patient())
        message["msg"] = pat_list
        return json.dumps(message)

    def create_patient(self, data):
        """Takes a json object and turns into a dictionary that is then passed
            to create a Patient object with the data. Returns a json value"""
                
        try:
            pronoun = int(data["pronoun"])
        except:
            pronoun = None
        
        try:
            message = {}
            p_split = data["email"].split("@")
            p_username = p_split[0]
            emails = []
            for patient in self.__patients:
                email = patient.get_patient_email()
                email_username = email.split("@")
                emails.append(email_username[0])
            if len(p_split) == 2 and p_split[1] != "" and p_split[0] not in emails:
                new_patient = Patient(p_username, data["name"], data["email"], data["note"], "", "", pronoun)
                self.__patients.append(new_patient)
                new_patient = new_patient.get_patient()
                message["msg"] = new_patient
                return json.dumps(message)
            else:
                return '{ "msg": "Not a valid email or email in use." }'
        except:
            return  '{ "msg": "Creating this patient was unsuccessful, please try again." }'
        
    def get_patient_info(self, data):
        """Returns a patient's information as a dictionary if it exists in the system"""
        try:
            message = {}
            for patient in self.__patients:
                if patient.get_patient_id() == data["username"]:
                    new_patient = patient.get_patient()
                    message["msg"] = new_patient
                    return json.dumps(message)     
            return '{"msg": "No patient with this"}'        
        except:
            return '{"msg": "No Patient Info"}'

    def delete_patient(self,data):
        """Deletes a patient with a particular username"""
        try:
            index = 0
            return_msg = {}
            for patient in self.__patients:
                if( data["username"] == patient.get_patient_id()):
                    return_msg["msg"] = patient.get_patient()
                    self.__patients.pop(index)
                    return json.dumps(return_msg)
                index += 1
            else:
                return '{"msg": "There is no patient with this username"}'
        except:
            return '{ "msg": "Deleting this patient was unsuccessful, please try again." }'

    def get_medical_history(self, data):
        """Returns a patients medical history if he has any"""
        try:
            data = json.loads(data)
            message = {}
            for patient in self.__patients:
                patient_id = patient.get_patient_id()
                if(data["patient"] == patient_id):
                    patient_records = patient.get_patient_records()
                    if patient_records == "":
                        patient_records = "No medical records"
                    message["msg"] = patient_records
                    message["username"] = patient_id
                    return json.dumps(message)     
            return '{"msg": "There is no patient with this username"}'        
        except:
            return '{"msg": "Retrieval of medical history unsuccessful"}'
