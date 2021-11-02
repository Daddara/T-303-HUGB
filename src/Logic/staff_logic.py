from data import Data
import json
from Classes.staff import Staff

class StaffLogic():
    def __init__(self):
        self.__data = Data()
        self.__staff = self.__data.get_staff()

    def get_patient_database(self):
        '''returns list of all staff from the database'''
        return self.__staff
    
    def create_staff(self, data):
        """Takes a json object and turns into a dictionary that is then passed
            to create a staff object with the data. Returns a json value"""
        try:
            message = {}
            staff_data = data["data"]
            
            # Check if name was inserted
            if staff_data["name"] == "":
                return '{"msg": "Staff member must have a name" }'

            # Check ssn
            try:
                ssn = int(staff_data["ssn"])
            except:
                return '{"msg": "Social security number must be numbers" }'

            # Check if ssn is correct length
            if len(staff_data["ssn"]) != 10:
                return '{"msg": "Social security number not of correct length" }'

            # Check if title was inserted
            if staff_data["title"] == "":
                return '{"msg": "Staff member must have a title" }'

            # Check if address was inserted
            if staff_data["address"] == "":
                return '{"msg": "Staff member must have an address" }'

            # Check if phone was inserted
            if staff_data["phone"] == "":
                return '{"msg": "Staff member must have a phone" }'

            new_staff = Staff(staff_data["name"], staff_data["ssn"], staff_data["title"], staff_data["address"], staff_data["phone"])
            self.__staff.append(new_staff)
            new_staff = new_staff.get_staff_member()
            message["msg"] = new_staff
            return json.dumps(message)
        except:
            return  '{"msg": "Creating this staff member was unsuccessful, please try again." }'
    
    def delete_staff_member(self,data):
        """Deletes a specific staff member by removing it from the data and returning it's information as a dict"""
        the_data = json.loads(data)
        index = 0
        for staff_member in self.__staff:
            if (the_data["staff_ssn"] == staff_member.get_staff()):
                return_msg = staff_member.get_staff_member()
                self.__staff.pop(index)
                return json.dumps(return_msg)
            index += 1
        else:
            return '{"msg":"No staff member with this ssn"}'