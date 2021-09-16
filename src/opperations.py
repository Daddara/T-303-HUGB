from HospitalSystem_if import Patients


Treatments = {"1": "Surgery", "2": "Catscan", "3": "x-rays", "4": "Bloodworks"}


class AssignTreatment:
    def __init__(self, patient=Patients, doctor=Doctors) -> None:
        self.patient_id = patient.id
        self.doctor_id = doctor.id
        self.appointment = None

    def assign_opperation(self, Treatments):
        self.appointment = Appointments(self.patient_id, self.doctor_id, Treatments[1])
        # Preferably, this will be a class that takes in patient id, doctor id('s),
        # and maybe a description? where the type of appointment will automatically be
        # "check-up", but can recieve text, that here will be the type of treatment maybe?

    def testing_print_result(self):
        if self.appointment:
            print("Appointment has been made.")


def main():
    random_test = AssignTreatment(
        "Patient of class Patients", "Doctor of class Doctors"
    )

    random_test.testing_print_result()