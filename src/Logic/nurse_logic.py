from data import Data
import json
from Classes.nurse import Nurse

class NurseLogic():
    def __init__(self):
        self.__data = Data()
        self.__nurses = self.__data.get_nurses()
    
    def get_nurse_database(self):
        """returns list of all nurses from the database"""
        return self.__nurses
    
    def create_nurse(self, data):
        """Creates a new instance of a Nurse"""
        try:
            message = {}
            nurse_data = data
            n_split = nurse_data["email"].split("@")
            emails = []
            for nurse in self.__nurses:
                email = nurse.get_nurse_email()
                email_username = email.split("@")
                emails.append(email_username[0])
            
            if str(nurse_data["username"]) not in emails and len(n_split) == 2 and n_split[1] != "" :
                new_nurse = Nurse(str(nurse_data["username"]), str(nurse_data["name"]), str(nurse_data["email"]), str(nurse_data["note"]))
                self.__nurses.append(new_nurse)
                new_nurse = new_nurse.get_info()
                message["msg"] = new_nurse
                return json.dumps(message)
            else:
                return '{"msg": "Not a valid email or email in use."}'
        except:
            return '{"msg": "Nurse not created"}'  

    def get_nurses_list(self):
        """Returns a list of all nurses"""
        message = {}
        nurse_list = []
        for nurse in self.__nurses:
            nurse_list.append(nurse.get_info())
        message["msg"] = nurse_list
        return json.dumps(message)

    def get_nurse(self, data):
        """Prints out nurse if it is in the system"""
        try:
            message = {}
            for nurse in self.__nurses:
                if nurse.get_username() == data["username"]:
                    new_nurse = nurse.get_info()
                    message["msg"] = new_nurse
                    return json.dumps(message)     
            return '{"msg": "No nurse with this username"}'        
        except:
            return '{"msg": No nurse Info"}'

    def update_nurse(self, data):
        """Updates information about an existing nurse."""
        try:
            if "username" in data:
                message = {}
                emails = []
                for nurse in self.__nurses:
                    email = nurse.get_nurse_email()
                    email_username = email.split("@")
                    emails.append(email_username[0])
                for nurse in self.__nurses:
                    username = data["username"]
                    if nurse.get_username() == username:
                        if "@" in data["email"]:
                            new_username = data["email"].split("@")
                            if new_username[1] != '':
                                emails.remove(nurse.get_username())
                                if new_username[0] not in emails:
                                    updated_nurse = nurse.update_nurse(new_username[0], data["name"], data["email"], data["note"])
                                else:
                                    updated_nurse = nurse.update_nurse(nurse.get_username(), data["name"], nurse.get_nurse_email(), data["note"])
                        json.dumps(message)
                message["msg"] = updated_nurse
                return json.dumps(message)

            else:
                return '{"msg": "username needed!"}'
        except:
            return  '{ "msg": "Updating this nurse was unsuccessful, please try again." }'
    
    def delete_nurse(self, data):
        """Gets the username of a nurse to be deleted and deletes the nurse."""
        try:
            counter = 0
            for nurse in self.__nurses:
                nurse_name = nurse.get_username()
                if(data["username"] == nurse_name):
                    return_message = nurse.get_info()
                    self.__nurses.pop(counter)
                    return json.dumps(return_message)
                counter += 1
            else:
                return '{"msg": "There is no nurse with this username"}'
        except:
            return '{ "msg": "It was unsuccessful at deleting the nurse." }'