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

    def update_patient(self, data):
        '''Updates information about an existing patient.'''
        try:
            if "username" in data:
                message = {}
                emails = []
                for patient in self.__patients:
                    email = patient.get_patient_email()
                    email_username = email.split("@")
                    emails.append(email_username[0])
                for patient in self.__patients:
                    username = data["username"]
                    if patient.get_patient_id() == username:
                        if "@" in data["email"]:
                            new_username = data["email"].split("@")
                            print(str(new_username))
                            if new_username[1] != '':
                                emails.remove(patient.get_patient_id())
                                if new_username[0] not in emails:
                                    updated_patient = patient.update_patient(new_username[0], data["name"], data["email"], data["note"])
                                else:
                                    updated_patient = patient.update_patient(patient.get_patient_id(), data["name"], patient.get_patient_email(), data["note"])
                            else:
                                print("Now here!!")
                        else:
                            print("Here!")
                        json.dumps(message)
                message["msg"] = updated_patient
                return json.dumps(message)

            else:
                return '{"msg": "username needed!"}'
        except:
            return  '{ "msg": "Updating this patient was unsuccessful, please try again." }'

    def send_presription(self, data):
        ''' This function takes in name of medicine and pharmecy along with the id of a patient.
        The function uses it to send a prescription for the medicine to the pharmecy for the patient. '''
        try:
            x = json.loads(data)
            for patient in self.__patients:
                if x["patient_id"] == patient.get_patient_id():
                    newPerscription = Prescription(x["medicine"], x["pharmecy"], x["patient_id"])
                    self.__prescriptions.append(newPerscription)
                    return_msg = newPerscription.get_return_str()
                    return return_msg
            else:
                return '{"msg": "Not a valid person"}'
        except:
            return '{"msg": "Order Failed"}'

    def get_patient_list(self):
        message = {}
        pat_list = []
        for patient in self.__patients:
            pat_list.append(patient.get_patient())
        message["msg"] = pat_list
        return json.dumps(message)

    def assign_treatment(self, data):
        data = json.loads(data)
        # See if the input patient exists
        patient_found = False
        for patient in self.__patients:
            patient_username = patient.get_patient_id()
            if patient_username == data["patient_username"]:
                appointment_patient = patient_username
                patient_found = True

        if patient_found == False:
            return '{"Patient with this username does not exist"}'

        # See if the assigned staff members exist
        staff_involved = []
        for staff_member in self.__staff:
            for assignee_ssn in data["staff"]:
                staff_member = staff_member.get_staff_member()
                if staff_member["ssn"] == assignee_ssn:
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
            new_appointment = new_appointment.get_info()
            return json.dumps(new_appointment)

        except:
            return '{"Appoinment was not created"}'
    
    def create_patient(self, data):
        """Takes a json object and turns into a dictionary that is then passed
            to create a Patient object with the data. Returns a json value"""
        
        try:
            message = {}
            # data = json.loads(data)
            print(data)
            # p_data = data["data"]
            # print(p_data)
            p_split = data["email"].split("@")
            print(p_split)
            # if "@" not in p_split:
            #     return '{ "msg": "Please enter a valid email" }'
            p_username = p_split[0]
            emails = []
            for patient in self.__patients:
                email = patient.get_patient_email()
                email_username = email.split("@")
                emails.append(email_username[0])

            print(emails)
            # if p_username == "":
            #     return '{ "msg": "Please enter a valid email" }'
            if len(p_split) == 2 and p_split[1] != "" and p_split[0] not in emails:
                new_patient = Patient(p_username, data["name"], data["email"], data["note"], "", "")
                self.__patients.append(new_patient)
                new_patient = new_patient.get_patient()
                message["msg"] = new_patient
                return json.dumps(message)
            else:
                return '{ "msg": "Not a valid email or email in use." }'
        except:
            return  '{ "msg": "Creating this patient was unsuccessful, please try again." }'
        
    def get_patient_info(self, data):
        "Prints out patient if it is listed in the system"
        try:
            message = {}
            for patient in self.__patients:
                if patient.get_patient_id() == data["username"]:
                    new_patient = patient.get_patient()
                    message["msg"] = new_patient
                    return json.dumps(message)     
            return '{"msg": "No Patient Info"}'        
        except:
            return '{"msg": No Patient Info"}'

    def delete_patient(self,data):
        """Deletes a patient with a particular ssn"""
        x = json.loads(data)
        index = 0
        for patient in self.__patients:
            if( x["patient_id"] == patient.get_patient_id()):
                return_msg = patient.get_patient()
                self.__patients.pop(index)
                return json.dumps(return_msg)
            index += 1
        else:
            return '{"msg":"No Patient with the id"}'
    
    def create_staff(self, data):
        """Takes a json object and turns into a dictionary that is then passed
            to create a staff object with the data. Returns a json value"""
        try:
            message = {}
            staff_data = data["data"]
            new_staff = Staff(staff_data["name"], staff_data["ssn"], staff_data["title"], staff_data["address"], staff_data["phone"])
            print(new_staff)
            self.__staff.append(new_staff)
            new_staff = new_staff.get_staff_member()
            message["msg"] = new_staff
            return json.dumps(message)
        except:
            return  '{"msg": "Creating this staff member was unsuccessful, please try again." }'
    
    def get_appointments(self, data):
        ''''iterates over all appointments and checks if the staff member ssn is in the appointment and then appends it to a list'''
        if "staff_ssn" in data:
            try:
                data = json.loads(data)
                id_counter = 1
                appointments_list = []
                message = {}
                for appoint in self.__appointments:
                    if appoint.check_appointments(str(data["staff_ssn"])):
                        x = appoint.get_info()
                        patient = x["patient"]
                        x["patient"] = patient.get_patient()
                        x["staff"] = len(x["staff"])
                        appointments_list.append(x)
                        id_counter += 1
                if len(appointments_list) != 0:
                    message["msg"] = appointments_list
                    return json.dumps(message)
                else:
                    return '{"msg":"No appointments"}'
            except:
                return '{"msg":"Invalid arguments, please try again}'
        else:
            return '{"msg":"Missing arguments: staff_ssn"}'


    def delete_staff_member(self,data):
        the_data = json.loads(data)
        # testing
        index = 0
        for staff_member in self.__staff:
            if (the_data["staff_ssn"] == staff_member.get_staff()):
                return_msg = staff_member.get_staff_member()
                self.__staff.pop(index)
                return json.dumps(return_msg)
            index += 1
        else:
            return '{"msg":"No staff member with this ssn"}'
