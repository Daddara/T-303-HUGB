from HospitalSystem_if import Patients


Treatments = {"1": "Surgery", "2": "Catscan", "3": "x-rays", "4": "Bloodworks"}


class AssignTreatment:
    def __init__(self, patient=Patients, doctor=Doctors, treatment_num=int) -> None:
        self.patient_id = patient.id
        self.doctor_id = doctor.id
        self.appointment = None
        self.treatment = Treatments[treatment_num]

    def assign_treatment(self):
        self.appointment = Appointments(
            self.patient_id, self.doctor_id, self.treatment, "Surgery on shoulder"
        )
        # Preferably, Appointments will be a class that takes in patient id, doctor id('s) (or specialists and nurses as well?),
        # type of treatment and maybe description? In appointments the type of treatment
        # will automatically be "check-up" maybe?

    def testing_print_result(self):
        if self.appointment:
            print("Appointment has been made.")
            print(
                "Patient with id " + self.patient_id + " has been assigned a treatment."
            )
            print("The treatment: " + self.treatment)
            print("Staff members assigned to the treatment: ")
        else:
            print("No appointment made.")


def main():
    random_test = AssignTreatment(
        "Patient of class Patients", "Doctor of class Doctors"
    )

    random_test.testing_print_result()