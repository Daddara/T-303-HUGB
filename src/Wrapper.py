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
        self.__doctors = self.__data.get_doctors()
        self.__nurses = self.__data.get_nurses()

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
                staff_member1 = staff_member.get_staff() # T breytti úr get_staff_member()
                if staff_member1 == assignee_ssn:
                    staff_involved.append(staff_member) # skilar semsagt object í stað dict

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
            new_appointment["staff"] = len(new_appointment["staff"]) #T breytti
            message = {}
            message["msg"] = new_appointment
            return json.dumps(message)

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
        try:
            index = 0
            return_msg = {}
            for patient in self.__patients:
                if( data["username"] == patient.get_patient_id()):
                    return_msg["msg"] = patient.get_patient()
                    print(index)
                    self.__patients.pop(index)
                    return json.dumps(return_msg)
                index += 1
            else:
                return '{"msg":"No Patient with the id"}'
        except:
            return '{ "msg": "Deleting this patient was unsuccessful, please try again." }'
    
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
                        # iterate over patients
                        
                        #change the staff object list to number of staff assigned
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

    def get_appointments_at_date(self, data):
        data = json.loads(data)

        doctor_found = False
        for doctor in self.__doctors:
            if doctor.get_username() == data["doctor"]:
                doctor_found = True
        
        if doctor_found == False:
            return '{"msg" : "No doctor has this username"}'

        from_date = data["from_date"]
        if len(from_date) != 3:
            return '{"msg" : "From date not of valid format"}'

        to_date = data["to_date"]
        if len(to_date) != 3:
            return '{"msg" : "From date not of valid format"}'

        try:
            int(from_date[0])
            int(from_date[1])
            int(from_date[2])
            int(to_date[0])
            int(to_date[1])
            int(to_date[2])
        except:
            return '{"msg" : "Please write date on integer format"}'
        
        id_counter = 1
        appointments_list = []
        message = {}
        for appoint in self.__appointments:
            appoint_dict = appoint.get_info()
            date = appoint_dict["date"]
            if appoint_dict["staff_involved"][0].get_username() != data["doctor"]:
                continue

            if (date[2] > from_date[3]) and (date[2] < to_date):
                #Year within limit
                appointments_list.append(appoint)
                continue
            elif (date[2] < from_date[3]) or (date[2] > to_date):
                #Year not within limit
                continue
            else:
                if (date[1] > from_date[1]) and (date[1] < to_date):
                    #month witin limit
                    appointments_list.append(appoint)
                    continue
                elif (date[1] < from_date[1]) or (date[1] > to_date):
                    #Month not within limit
                    continue
                else: 
                    if (date[0] > from_date[0]) and (date[0] < to_date):
                        #day within limit
                        appointments_list.append(appoint)
                        continue
                    elif (date[0] < from_date[0]) or (date[0] > to_date):
                        #day within limit
                        continue
                    else:
                        continue
 
        if len(appointments_list) != 0:
            message["msg"] = appointments_list
            return json.dumps(message)
        else:
            return '{"msg":"No appointments"}'

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


    # doctor methods

    def get_doctors_list(self):
        """returns list of all nurses"""
        message = {}
        doc_list = []
        for doctor in self.__doctors:
            doc_list.append(doctor.get_info())
        message["msg"] = doc_list
        return json.dumps(message)

    def get_doctor(self, data):
        """returns doctor if it is listed in the system"""
        try:
            message = {}
            for doctor in self.__doctors:
                print(doctor.get_username())
                print(data["username"])
                if doctor.get_username() == data["username"]:
                    new_doctor = doctor.get_info()
                    message["msg"] = new_doctor
                    return json.dumps(message)     
            return '{"msg": "No Doctor Info"}'        
        except:
            return '{"msg": No Doctor Info"}'



    # nurse methods

    def get_nurses_list(self):
        """returns list of all nurses"""
        message = {}
        nurse_list = []
        for nurse in self.__nurses:
            nurse_list.append(nurse.get_info())
        message["msg"] = nurse_list
        return json.dumps(message)

    def get_nurse(self, data):
        """Prints out nurse if it is listed in the system"""
        try:
            message = {}
            for nurse in self.__nurses:
                if nurse.get_username() == data["username"]:
                    new_nurse = nurse.get_info()
                    message["msg"] = new_nurse
                    return json.dumps(message)     
            return '{"msg": "No nurse Info"}'        
        except:
            return '{"msg": No nurse Info"}'

