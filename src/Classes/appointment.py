from Classes.patient import Patient


# Treatments used for first implementation. Each treatment has an id. List will get longer.
TREATMENTS = {
    1: "Checkup",
    2: "Surgery",
    3: "Catscan",
    4: "x-rays",
    5 : "Bloodworks",
}


class Appointment:
    """This class keeps track of appointments."""
    def __init__(self, patient:str, list_of_staff:list, date:list, time:str, duration:int, treatment=None, description=None) -> None:
        # If a treatment is not declared it is automatically a checkup
        if treatment == None:
            treatment = TREATMENTS[1]
        else:
            treatment = TREATMENTS[treatment]

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
        """Returns a dictionary that contains the information about the appointment"""
        appointment_info = {"patient": self.patient, "staff": self.staff_involved, "date": self.date, "time": self.time, "duration": self.duration, "treatment": self.treatment, "description": self.description}
        return appointment_info


    def check_appointments(self, staff_ssn) -> bool:
        """Returns a boolean value on whether a certain staff member is assigned to an appointment"""
        for staff in self.staff_involved:
            if staff.get_staff() == staff_ssn:
                return True
        return False

    def check_doctor(self, username) -> bool:
        """Returns a boolean value on whether a certain doctor is assigned to an appointment"""
        for doctor in self.staff_involved:
            if doctor == username:
                return True
        return False

    def get_date(self) -> list:
        """Returns the date of the appointment"""
        return self.date
