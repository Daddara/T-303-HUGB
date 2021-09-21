from Classes.appointment import TREATMENTS, Appointment
from HospitalSystem_client import assign_treatment
from data import Data
from Classes.patient import Patient
import json


class Wrapper:
    def __init__(self):
        self.__data = Data()
        self.__patients = self.__data.get_patients()  # return list of dict
        self.__staff = self.__data.get_staff()  #
        self.__appointments = self.__data.get_appointments()
        self.__prescriptions = self.__data.get_prescriptions()

    def send_presription(self, data):
        try:
            self.hospital.PharmacyRequests.append(
                [
                    self.pharmecy.get_pharmecy(data[0]),
                    self.patient.get_patient(data[2]),
                    self.medicine.get_medicine(data[4]),
                ]
            )
            print(
                "The requests for the pharmecy are now: "
                + str(self.pharmecy.PharmecyRequests)
            )

            return (
                '{"Order for medicine:'
                + str(self.pharmecy.PharmecyRequests[0][2][0])
                + " to pharmacy: "
                + str(self.pharmecy.PharmecyRequests[0][0])
                + " for patient: "
                + str(self.pharmecy.PharmecyRequests[0][1][0])
                + " }"
            )
        except:
            return '{"Order Failed"}'

    def get_patient_list(self, data):
        self.__patients.get_patient_list(data)
        return '{"Not implemented"}'

    def assign_treatment(self, data):
        data = json.loads(data)
        # See if the input patient exists
        for patient in self.__patients:
            if patient.__p_ssn == data["ssn"]:
                appointment_patient = patient
            else:
                return '{"Patient with this social security number does not exist"}'

        # See if the assigned staff members exist
        staff_involved = []
        for staff_member in self.__staff:
            for assignee_ssn in data["staff"]:
                if staff_member.__ssn == assignee_ssn:
                    staff_involved.append(staff_member)
        if len(staff_involved) == 0:
            return '{"At least one staff member whose social security number was input does not exist."}'

        # See if duration can be converted to an integer
        try:
            duration = int(data["duration"])
        except:
            return '{"Duration must be a number (minutes)"}'

        # Take the integer of the treatment chosen, if it doesn't work, then the treatment is automatic "Checkup"
        try:
            treatment = int(data["treatment"])
        except:
            treatment = None

        try:
            new_appointment = Appointment(appointment_patient, staff_involved, data["date"], data["time"], duration, treatment, data["description"])
            self.__appointments.append(new_appointment)
            print("APPOINTMENT CREATED")
            new_appointment = new_appointment.get_info()
            return json.dumps(new_appointment)

        except:
            return '{"Appoinment was not created"}'
    
    def create_patient(self, data):
        data = json.loads(data)
        try:
            new_patient = Patient(data["ssn"], data["name"], data["address"], data["phone"], data["email"], data["record"])
            print("PATIENT CREATED")
            print(new_patient.get_patient())
            new_patient = new_patient.get_patient()
            return json.dumps(new_patient)
        except:
            return  '{ "No!!!!!" }'
        
    
    def get_patient_info(self, data):
        "Prints out patient if it is listed in the system"
        try:
            for patient in self.__patients:
                if patient.get_patient_id() == data:
                    new_patient = patient.get_patient()
                    patient_list = ("Name: " + str(new_patient[0]) + "\nSSN: " + str(new_patient[1]) + "\nAddress: " + str(new_patient[2]) + "\nPhone: " + str(new_patient[3]) + "\nEmail: " + str(new_patient[4]))
                    return patient_list
        except:
            return '{"No Patient Info"}'

    def delete_patient(self,data):
        
        index = 0
        for dict in self.__patients:
            index +=1
            if( dict[data] == id):
                deleted_patient = self.__patients.pop(dict)
        
        return json.dumps(deleted_patient)
