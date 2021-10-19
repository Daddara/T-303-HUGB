# Autogenerated from websocket_interface.template file
from Wrapper import Wrapper


class HospitalsystemInterface:

    def __init__(self):
        self.wrapper = Wrapper()
        print("Welcome to the Hospital System!")

    # Staff

    def delete_staff_member(self, data):
        """Deletes a staff member"""
        return self.wrapper.delete_staff_member(data)

    def create_staff(self, data): 
        '''Creates a staff member'''    
        return_msg = self.wrapper.create_staff(data)
        return return_msg

    # Patients

    def readAll_patient (self, data):
        """Returns a list of all patients"""
        return self.wrapper.get_patient_list()

    def get_patient_info (self, data):
        """Returns all info about a specific patient"""
        return_msg = self.wrapper.get_patient_info(data)
        return return_msg

    def create_patient(self, data):    
        """Creates a patient""" 
        #Here you call the actual operation in your backend code.
        return_msg = self.wrapper.create_patient(data)
        return return_msg

    def get_patient_list(self, data):
        """Lists all patients"""
        return self.wrapper.get_patient_list(data)

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

    # Doctors

    def readAll_doctor(self, data):
        """Gets all doctors"""
        return self.wrapper.get_doctors_list()
    
    def read_doctor(self, data):
        """Gets info about a doctor as a dict"""
        return self.wrapper.get_doctor(data)

    def update_doctor (self, data):
        """Updates info about a doctor"""
        return self.wrapper.update_doctor(data)

    def create_doctor(self, data):
        """Creates a doctor"""
        return_msg = self.wrapper.create_doctor(data)
        return return_msg
    
    # Nurses

    def readAll_nurse(self, data):
        """Gets a list of all nurses"""
        return self.wrapper.get_nurses_list()

    def read_nurse(self, data):
        """Gets info about a nurse as a dict"""
        return self.wrapper.get_nurse(data)

    def update_nurse(self, data):
        """Updates info about a nurse"""
        return self.wrapper.update_nurse(data)

    def create_nurse(self, data): 
        '''Creates a nurse'''    
        return_msg = self.wrapper.create_nurse(data)
        return return_msg

    def delete_nurse(self, data):
        """Deletes a nurse from the data"""
        return self.wrapper.delete_nurse(data)

    # Other
    
    def get_patient_appointments(self, data):
        """Returns all apointments which a staff member is assigned to"""
        return self.wrapper.get_appointments(data)

    def get_appointments_at_date(self, data):
        """Returns all appointments a doctor is assigned to at a specific date"""
        return self.wrapper.get_appointments_at_date(data)

    def send_presription(self, data):
        """Creates a prescription"""
        return_msg = self.wrapper.send_presription(data)
        return return_msg

    def assign_treatment(self, data):
        """Assignes a treatment to a patient"""
        return self.wrapper.assign_treatment(data)