import json
from Classes.appointment import Appointment
from Classes.prescription import Prescription
from data import Data
from Classes.patient import Patient
from Classes.staff import Staff


class Wrapper:
    def __init__(self):
        self.__data = Data()
        self.__patients = self.__data.get_patients()  # return list of dict
        self.__staff = self.__data.get_staff()  #
        self.__appointments = self.__data.get_appointments()
        self.__prescriptions = self.__data.get_prescriptions()

    def send_presription(self, data):
        try:
            x = json.loads(data)
            newPerscription = Prescription(x["medicine"], x["pharmecy"], x["patient_id"])
            # print(self.__prescriptions)
            self.__prescriptions.append(newPerscription)
            # print(self.__prescriptions)
            return_msg = newPerscription.get_return_str()
            return return_msg
        except:
            return '{"Order Failed"}'

    def get_patient_list(self):
        print(self.__patients)
        patient_list = []
        for patient in self.__patients:
            patient_list.append(patient.get_patient())
            print(patient_list)
        return json.dumps(patient_list)

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
        """Takes a json object and turns into a dictionary that is then passed
            to create a Patient object with the data. Returns a json value"""

        data = json.loads(data)
        try:
            new_patient = Patient(data["ssn"], data["name"], data["address"], data["phone"], data["email"], data["record"])
            self.__patients.append(new_patient)
            new_patient = new_patient.get_patient()
            return json.dumps(new_patient)
        except:
            return  '{ "Creating this patient was unsuccessful, please try again." }'
        
    def get_patient_info(self, data):
        "Prints out patient if it is listed in the system"
        try:
            x = json.loads(data)
            for patient in self.__patients:
                if patient.get_patient_id() == x["patient_id"]:
                    new_patient = patient.get_patient()
                    return new_patient
        except:
            return '{"No Patient Info"}'

    def delete_patient(self,data):
    
        index = 0
        for dict in self.__patients:
            index +=1
            if( dict[data] == id):
                deleted_patient = self.__patients.pop(dict)
        
        return json.dumps(deleted_patient)
    
    def get_appointments(self, data):
        ''''iterates over all appointments and checks if the staff member ssn is in the appointment and then appends it to a list'''
        if "staff_ssn" in data:
            data = json.loads(data)
            id_counter = 1
            appointments_list = {}
            for appoint in self.__appointments:
                print(data["staff_ssn"])
                if appoint.check_appointments(str(data["staff_ssn"])):
                    appointments_list[str(id_counter)] = appoint.get_info()
                    id_counter += 1
            if len(appointments_list) != 0:
                return '{"msg":"nice one"}'
            else:
                return '{"msg":"No appointmentsA"}'
        else:
            return '{"msg":"No appointments"}'

