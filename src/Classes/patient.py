import json

class Patient():
  
    def __init__(self, name:str, ssn:str, address=None, phone=None, email=None):
        self.name = name
        self.ssn = ssn
        self.address = address
        self.phone = phone 
        self.email = email

    def get_patient_id(self):
        return self.ssn

    def get_patient(self):
        ''' Gets all patients'''
        # patient_dict = {
        #     "name": self.name,
        #     "age": self.age,
        #     "ssn": self.ssn, 
        #     "address": self.address, 
        #     "phone": self.phone, 
        #     "email": self.email
        # }
        
        patient_list = [self.name, self.ssn, self.address, self.phone, self.email]
        
        return patient_list
