import json

class Patient():
  
    def __init__(self, name:str, ssn:str, address:str, phone:str, email:str):
        self.name = name
        self.ssn = ssn
        self.address = address
        self.phone = phone 
        self.email = email

    def get_patient_id(self):
        return self.ssn

    def get_patient(self):
        ''' Gets all patients'''
        patient_dict = {
            "name": self.name,
            "ssn": self.ssn,
            "address": self.address, 
            "phone": self.phone, 
            "email": self.email
        }
        
        return json.dumps(patient_dict)
