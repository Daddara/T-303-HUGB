import json

class Prescription:
    """This class keeps track of prescriptions made"""
    def __init__(self, medicine_name:str, pharmecy_name:str, patient_id:str):
        self.medicine_name = medicine_name
        self.pharmecy_name = pharmecy_name
        self.patient_id = patient_id

    def get_medicine_name(self):
        """Returns the name of the medicine being prescribed"""
        return self.medicine_name

    def get_pharmecy_name(self):
        """Returns the name of the pharmacy"""
        return self.pharmecy_name
    
    def get_patient_id(self):
        """Returns the id (username) of the patient who's getting the prescription"""
        return self.patient_id

    def get_return_str(self):
        """Returns the information about the prescription in a dictionary"""
        prescription_data = {
            "medicine": self.medicine_name,
            "pharmecy": self.pharmecy_name,
            "patient_id": self.patient_id

        }
        return json.dumps(prescription_data)
