import json

class Staff():

    def __init__(self, name:str, ssn:str, title:str, address=None, phone=None):
        self.__name = name
        self.__ssn = ssn
        self.__title = title
        self.__address = address
        self.__phone = phone        # can be empty (þarf kannski að vera fyrir starfsmann)

    def get_staff_member(self, ssn):
        ''' Searches for staff member on ssn and then returns json of all it's attributes'''
        staff_dict = {
            "name": self.__name,
            "age": self.__age,
            "ssn": self.__ssn,  
            "address": self.__address, 
            "phone": self.__phone, 
            "title": self.__title,
            "hospitalName": self.__hospital_name
        }
        return json.dumps(staff_dict)
