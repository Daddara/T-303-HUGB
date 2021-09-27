# Autogenerated from websocket_interface.template file
from Wrapper import Wrapper


class HospitalsystemInterface:

    def __init__(self):
        self.wrapper = Wrapper()
        print("Welcome to the Hospital System!")

    def readAll_patient (self, data):
        return '{"msg": [{"name": "Patient 1", "email": "patient1@email.com", "note": "Dummy note", "username": "patient1", "doctor_id": "null", "nurse_id": "null"}, {"name": "patient 2", "email": "patient2@email.com", "note": "this is a dummy note", "username": "patient2", "doctor_id": "null", "nurse_id": null}]}' 

    def get_patient_info (self, data):
        return_msg = self.wrapper.get_patient_info(data)
        return return_msg

            
    def get_patient_appointments (self, data):
        return self.wrapper.get_appointments(data)

    def delete_patient(self, data):     
        #Here you call the actual operation in your backend code.
        return self.wrapper.delete_patient(data)

    def send_presription(self, data):
        return_msg = self.wrapper.send_presription(data)
        return return_msg

    def create_patient(self, data):     
        #Here you call the actual operation in your backend code.
        return_msg = self.wrapper.create_patient(data)
        return return_msg

    def get_patient_list(self, data):
        return self.wrapper.get_patient_list(data)

    def assign_treatment(self, data):
        return self.wrapper.assign_treatment(data)

    def delete_staff_member(self, data):
        return self.wrapper.delete_staff_member(data)
