from Classes.patient import Patient
from Classes.staff import Staff
from data import Data
import json


# Treatments used for first implementation. Each treatment has an id. List will get longer.
TREATMENTS = {
    1: "Regular checkup",
    2: "Surgery",
    3: "Catscan",
    4: "x-rays",
    5 : "Bloodworks",
}


class Appointment:
    def __init__(self, patient:Patient, list_of_staff:list, date:list, time:str, duration:int, treatment=None, description=None) -> None:
        if treatment == None:
            treatment = TREATMENTS[1]

        if description == None:
            description = ""
        
        self.patient = patient
        self.staff_involved = list_of_staff
        self.date = date
        self.time = time
        self.duration = duration
        self.treatment = treatment
        self.description = description
        
        
    def get_info(self) -> dict:
        appointment_info = {"patient": self.patient, "staff": self.staff_involved, "date": self.date, "time": self.time, "duration": self.duration, "treatment": self.treatment, "descpription": self.description}
        return json.dumps(appointment_info)


    def check_doctor(self, doctor_ssn) -> bool:
        for staff in self.staff_involved:
            if staff.ssn == doctor_ssn:
                return True

        return False