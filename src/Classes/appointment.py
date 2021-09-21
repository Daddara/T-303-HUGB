from typing import List
from Classes.patient import Patient
from Classes.staff import Staff
from data import Data

TREATMENTS = {
    "1": "Regular checkup",
    "2": "Surgery",
    "3": "Catscan",
    "4": "x-rays",
    "5": "Bloodworks",
}


class Appointment:
    def __init__(
        self,
        patient=Patient,
        list_of_staff=List,
        date=list,
        time=int,
        duration=int,
        treatment=int,
    ) -> None:
        self.patient = patient
        self.staff_involved = list_of_staff
        self.date = date
        self.time = time
        self.duration = duration
        if treatment == None:
            self.treatment = TREATMENTS[1]
        else:
            self.treatment = treatment
