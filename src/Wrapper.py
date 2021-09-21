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

    def get_patient_list(self, data):
        self.__patients.get_patient_list(data)
        return '{"Not implemented"}'

    def assign_treatment(self, data):
        data = json.loads(data)
        # See if the input patient exists
        patient_found = False
        for patient in self.__patients:
            patient = patient.get_patient()
            print(data["patient_ssn"])
            print(patient["ssn"])
            if patient["ssn"] == data["patient_ssn"]:
                appointment_patient = patient
                patient_found = True

        if patient_found == False:
            return '{"Patient with this social security number does not exist"}'

        # See if the assigned staff members exist
        staff_involved = []
        for staff_member in self.__staff:
            print(data["staff"])
            for assignee_ssn in data["staff"]:
                print(assignee_ssn)
                staff_member = staff_member.get_staff_member()
                if staff_member["ssn"] == assignee_ssn:
                    print(staff_member["ssn"])
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
<<<<<<< HEAD
                    return json.dumps(new_patient)
        except ValueError:
            return '{"No Patient Info"}'
=======
                    return new_patient
        except:
            return '{"msg": "No Patient Info"}'
>>>>>>> origin/back1

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
            try:
                data = json.loads(data)
                id_counter = 1
                appointments_list = []
                appointments_dict = {}
                for appoint in self.__appointments:
                    print(data["staff_ssn"])
                    if appoint.check_appointments(str(data["staff_ssn"])):
                        x = appoint.get_info()
                        patient = x["patient"]
                        x["patient"] = patient.get_patient()
                        x["staff"] = len(x["staff"])
                        print(x)
                        appointments_list.append(x)
                        id_counter += 1
                if len(appointments_list) != 0:
                    return json.dumps(appointments_list)
                else:
                    return '{"msg":"No appointments"}'
            except:
                return '{"msg":"Invalid arguments, please try again}'
        else:
            return '{"msg":"No appointments"}'
