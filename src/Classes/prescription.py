import json

class Prescription:
    def __init__(self, medicine_name:str, pharmecy_name:str, patient_id:str):
        self.medicine_name = medicine_name
        self.pharmecy_name = pharmecy_name
        self.patient_id = patient_id

    def get_medicine_name(self):
        return self.medicine_id

    def get_pharmecy_name(self):
        return self.pharmecy_name
    
    def get_patient_id(self):
        return self.patient_id

    def get_return_str(self):
        prescription_data = {
            "medicine": self.medicine_name,
            "pharmecy": self.pharmecy_name,
            "patient_id": self.patient_id

        }
        return json.dumps(prescription_data)

    def send_prescription(self):
        pass