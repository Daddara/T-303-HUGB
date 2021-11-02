from data import Data
import json
from Classes.doctor import Doctor

class DoctorLogic():
    def __init__(self):
        self.__data = Data()
        self.__doctors = self.__data.get_doctors()
    
    def get_doctor_database(self):
        '''returns list of all doctors from the database'''
        return self.__doctors
    
    def create_doctor(self, data):
        """Takes a json object and turns into a dictionary that is then passed
            to create a Patient object with the data. Returns a json value"""     
        try:
            message = {}
            d_split = data["email"].split("@")
            emails = []
            for doctor in self.__doctors:
                email = doctor.get_doctor_email()
                email_username = email.split("@")
                emails.append(email_username[0])
            if str(data["username"]) not in emails:
                new_doctor = Doctor(str(data["username"]), str(data["name"]), str(data["email"]), str(data["note"]), "")
                self.__doctors.append(new_doctor)
                new_doctor = new_doctor.get_info()
                message["msg"] = new_doctor
                return json.dumps(message)
            else:
                return '{ "msg": "Not a valid email or email in use." }'
        except:
            return  '{ "msg": "Creating this doctor was unsuccessful, please try again." }'

    def get_doctors_list(self):
        """Returns a list of all doctors"""
        message = {}
        doc_list = []
        for doctor in self.__doctors:
            doc_list.append(doctor.get_info())
        message["msg"] = doc_list
        return json.dumps(message)

    def get_doctor(self, data):
        """returns doctor if it is in the system"""
        try:
            message = {}
            for doctor in self.__doctors:
                if doctor.get_username() == data["username"]:
                    new_doctor = doctor.get_info()
                    message["msg"] = new_doctor
                    return json.dumps(message)     
            return '{"msg": "No doctor with this username"}'        
        except:
            return '{"msg": "No Doctor Info"}'
    
    def delete_doctor(self, data):
        """Deletes a doctor with a particular username"""
        index = 0
        for doctors in self.__doctors:
            if data["username"] == doctors.get_username():
                return_msg = doctors.get_info()
                self.__doctors.pop(index)
                return json.dumps(return_msg)
            index += 1
        else:
            return '{"msg": "There is no doctor with this username"}'

    def update_doctor (self, data):
        """Updates information about an existing doctor."""
        try:
            if "username" in data:
                message = {}
                emails = []
                for doctor in self.__doctors:
                    email = doctor.get_doctor_email()
                    email_username = email.split("@")
                    emails.append(email_username[0])
                for doctor in self.__doctors:
                    username = data["username"]
                    if doctor.get_username() == username:
                        if "@" in data["email"]:
                            new_username = data["email"].split("@")
                            if new_username[1] != '':    
                                emails.remove(doctor.get_username())
                                if new_username[0] not in emails:
                                    updated_doctor = doctor.update_doctor(new_username[0], data["name"], data["email"], data["note"], data["department"])
                                else:
                                    updated_doctor = doctor.update_doctor(doctor.get_username(), data["name"], doctor.get_doctor_email(), data["note"], data["department"])
                        json.dumps(message)
                message["msg"] = updated_doctor
                return json.dumps(message)

            else:
                return '{"msg": "username needed!"}'
        except:
            return  '{ "msg": "Updating this doctor was unsuccessful, please try again." }'