# Autogenerated from websocket_interface.template file
from Wrapper import Wrapper


class HospitalsystemInterface:

    def __init__(self):
        self.wrapper = Wrapper()
        print("Welcome to the Hospital System!")

    def readAll_patient (self, data):
        """Returns a list of all patients"""
        return self.wrapper.get_patient_list()

    def get_patient_info (self, data):
        """Returns all info about a specific patient"""
        return_msg = self.wrapper.get_patient_info(data)
        return return_msg

    def get_patient_appointments(self, data):
        """Returns all apointments which a staff member is assigned to"""
        return self.wrapper.get_appointments(data)

    def read_patient(self, data):
        """Returns all info to the frontend about a specific patient"""
        return self.wrapper.get_patient_info(data)
    
    def update_patient(self, data):
        """Updates information about a patient"""
        return self.wrapper.update_patient(data)

    def delete_patient(self, data):
        """Deletes a specific patient"""     
        #Here you call the actual operation in your backend code.
        return self.wrapper.delete_patient(data)

    def send_presription(self, data):
        """Creates a prescription"""
        return_msg = self.wrapper.send_presription(data)
        return return_msg

    def create_patient(self, data):    
        """Creates a patient""" 
        #Here you call the actual operation in your backend code.
        return_msg = self.wrapper.create_patient(data)
        return return_msg

    def create_doctor(self, data):
        """Creates a doctor"""
        return_msg = self.wrapper.create_doctor(data)
        return return_msg

    def get_patient_list(self, data):
        """Lists all patients"""
        return self.wrapper.get_patient_list(data)

    def assign_treatment(self, data):
        """Assignes a treatment to a patient"""
        return self.wrapper.assign_treatment(data)

    def delete_staff_member(self, data):
        """Deletes a staff member"""
        return self.wrapper.delete_staff_member(data)

    def create_staff(self, data):     
        return_msg = self.wrapper.create_staff(data)
        return return_msg

    # Doctors

    def readAll_doctor(self, data):
        return self.wrapper.get_doctors_list()
    
    def read_doctor(self, data):
        return self.wrapper.get_doctor(data)
    
    # Nurses

    def readAll_nurse(self, data):
        return self.wrapper.get_nurses_list()

    def read_nurse(self, data):
        return self.wrapper.get_nurse(data)