# Autogenerated from websocket_interface.template file
from Wrapper import Wrapper


class HospitalsystemInterface:

    def __init__(self):
        self.wrapper = Wrapper()
        print("Welcome to the Hospital System!")

    def get_patient_info (self, data):
        return_msg = self.wrapper.get_patient_info(data)
        return return_msg
            
    def get_patient_appointments (self, data):
        return self.wrapper.get_appointments(data)

    def delete_patient (self, data):
        if "patient_id" in data :      
            #Here you call the actual operation in your backend code.
            return '{"msg":"Operation delete_patient not yet implemented"}'
        else:
            return '{"msg":"Invalid request. The following parameters are required: patient_id."}' 

    def send_presription (self, data):
        return_msg = self.wrapper.send_presription(data)
        return return_msg

    def create_patient (self, data):     
        #Here you call the actual operation in your backend code.
        return_msg = self.wrapper.create_patient(data)
        return return_msg

    def get_patient_list (self, data):
        return self.wrapper.get_patient_list(data)

    def assign_treatment(self, data):
        return self.wrapper.assign_treatment(data)
