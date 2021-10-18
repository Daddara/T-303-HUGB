import json
from Classes.appointment import Appointment
from Classes.doctor import Doctor
from Classes.prescription import Prescription
from data import Data
from Classes.patient import Patient
from Classes.staff import Staff
from Classes.nurse import Nurse

class Wrapper:
    def __init__(self):
        self.__data = Data()
        self.__patients = self.__data.get_patients()  
        self.__staff = self.__data.get_staff()  
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
                            if new_username[1] != '':
                                emails.remove(patient.get_patient_id())
                                if new_username[0] not in emails:
                                    updated_patient = patient.update_patient(new_username[0], data["name"], data["email"], data["note"])
                                else:
                                    updated_patient = patient.update_patient(patient.get_patient_id(), data["name"], patient.get_patient_email(), data["note"])
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
        """Returns all patients' info as dictionaries"""
        message = {}
        pat_list = []
        for patient in self.__patients:
            pat_list.append(patient.get_patient())
        message["msg"] = pat_list
        return json.dumps(message)

    def assign_treatment(self, data):
        """Assigns an appointment to a patient"""
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
        for doctor in self.__doctors:
            for doc_username in data["staff"]:
                doctor_user = doctor.get_username()
                if doctor_user == doc_username:
                    staff_involved.append(doc_username) 

        if len(staff_involved) == 0:
            return '{"A doctor with this username does not exist."}'

        # See if duration can be converted to an integer
        try:
            duration = int(data["duration"])
        except:
            return '{"Duration must be a number (minutes)"}'
        
        # See if the time is valid
        try:
            time = data["time"].split(":")
            hour = int(time[0])
            minute = int(time[1])
        except:
            return '{"Time not of valid format"}'

        if hour < 0 or hour > 24:
            return '{"Time not valid. Hour needs to be between 00 - 24"}'
        if minute < 0 or minute > 59:
            return '{"Time not valid. Minutes need to be between 00 - 59"}'

        # See if date is valid
        date = data["date"]
        if len(date) != 3:
            return '{"Date must be entered on format DD MM YYYY"}'
        try:
            day = int(date[0])
            month = int(date[1])
            year = int(date[2])
        except:
            return '{"Date must be entered as numbers"}'

        if day < 0 or day > 31:
            return '{"Day cannot be smaller than 0 or larger than 31"}'
        if month < 1 or month > 12:
            return '{"Month cannot be smaller than 1 or larger than 12"}'
        if month == 2 and day > 29:
            return '{"Febuary only has at most 29 days. Please check the inserted dates"}'
        if year < 2015 or year > 2050:
            return '{"You cant add an appointment further in the past than 2015, or further in the future than 2050"}'
            

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
            p_split = data["email"].split("@")
            p_username = p_split[0]
            emails = []
            for patient in self.__patients:
                email = patient.get_patient_email()
                email_username = email.split("@")
                emails.append(email_username[0])
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
        

    def create_doctor(self, data):
        """Takes a json object and turns into a dictionary that is then passed
            to create a Patient object with the data. Returns a json value"""
        
        try:
            message = {}
            d_split = data["email"].split("@")
            emails = []
            for doctor in self.__doctors:
                email = doctor.get_email()
                email_username = email.split("@")
                emails.append(email_username[0])
            if str(data["username"]) not in emails:
                new_doctor = Doctor(str(data["username"]), str(data["name"]), str(data["email"]), str(data["note"]), "")
                self.__doctors.append(new_doctor)
                new_doctor = new_doctor.get_info()
                message["msg"] = new_doctor
                return json.dumps(message)
            else:
                return '{ "msg": "Not a valid email or email in use." }'
        except:
            return  '{ "msg": "Creating this doctor was unsuccessful, please try again." }'
    

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
            self.__staff.append(new_staff)
            new_staff = new_staff.get_staff_member()
            message["msg"] = new_staff
            return json.dumps(message)
        except:
            return  '{"msg": "Creating this staff member was unsuccessful, please try again." }'
    
    """creates a Nurse"""
    def create_nurse(self, data):

        try:
            message = {}
            nurse_data = data
            n_split = nurse_data["email"].split("@")
            emails = []
            for nurse in self.__nurses:
                email = nurse.get_nurse_email()
                email_username = email.split("@")
                emails.append(email_username[0])
            
            if str(nurse_data["username"]) not in emails and len(n_split) == 2 and n_split[1] != "" :
                new_nurse = Nurse(str(nurse_data["username"]), str(nurse_data["name"]), str(nurse_data["email"]), str(nurse_data["note"]))
                self.__nurses.append(new_nurse)
                new_nurse = new_nurse.get_info()
                message["msg"] = new_nurse
                return json.dumps(message)
            else:
                return '{ "msg": "Not a valid email or email in use." }'
        except:
            return  '{"msg": "Creating this nurse was unsuccessful, please try again." }'
        
    
    def get_appointments(self, data):
        ''''iterates over all appointments and checks if the staff member ssn is in the appointment and then appends it to a list'''
        if "username" in data:
            try:
                data = json.loads(data)
                id_counter = 1
                appointments_list = []
                message = {}
                for appoint in self.__appointments:
                    if appoint.check_doctor(data["username"]):
                        x = appoint.get_info()
                        # iterate over patients
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
        """
        Returns all appointments as a dictionary if they belong to the inserted doctor
        and if the date of the appointment is within searching range
        """
        data = json.loads(data)

        # Check if the username belongs to a doctor in the database
        doctor_found = False
        for doctor in self.__doctors:
            if doctor.get_username() == data["doctor"]:
                doctor_found = True
        
        if doctor_found == False:
            return '{"msg" : "No doctor has this username"}'
        
        # See if the inserted dates are valid
        from_date = data["from_date"]
        if len(from_date) != 3:
            return '{"msg" : "From date not of valid format"}'

        to_date = data["to_date"]
        if len(to_date) != 3:
            return '{"msg" : "From date not of valid format"}'

        try:
            day = int(from_date[0])
            month = int(from_date[1])
            year = int(from_date[2])
            day2 = int(to_date[0])
            month2 = int(to_date[1])
            year2 = int(to_date[2])
        except:
            return '{"msg" : "Please write date on integer format"}'

        if day < 0 or day > 31 or day2 < 0 or day2 > 31:
            return '{"Day cannot be smaller than 0 or larger than 31."}'
        if month < 1 or month > 12 or month2 < 1 or month2 > 12:
            return '{"Month cannot be smaller than 1 or larger than 12."}'
        if (month == 2 and day > 29) or (month2 == 2 and day2 > 29):
            return '{"Febuary only has at most 29 days. Please check the inserted dates."}'
        if year < 2015 or year > 2050 or year2 < 2015 or year2 > 2050:
            return '{"You cant add an appointment further in the past than 2015, or further in the future than 2050."}'
        

        # Start searching for appointments
        appointments_list = []
        message = {}
        for appoint in self.__appointments:
            appoint_dict = appoint.get_info()
            doctor = appoint_dict["staff"][0]
            if doctor != data["doctor"]:
                continue
            
            date = appoint.get_date()

            if (int(date[2]) > int(from_date[2])) and (int(date[2]) < int(to_date[2])):
                #Year within limit
                appointments_list.append(appoint_dict)
                continue

            elif (int(date[2]) < int(from_date[2])) or (int(date[2]) > int(to_date[2])):
                #Year not within limit
                continue
            else:
                # Check month
                if (int(date[1]) > int(from_date[1])) and (int(date[1]) < int(to_date[1])):
                    #month witin limit
                    appointments_list.append(appoint_dict)
                    continue
                elif (int(date[1]) < int(from_date[1])) or (int(date[1]) > int(to_date[1])):
                    #Month not within limit
                    continue
                else: 
                    #Check day
                    if (int(date[0]) >= int(from_date[0])) and (int(date[0]) <= int(to_date[0])):
                        #day within limit
                        appointments_list.append(appoint_dict)
                        continue
                    elif (int(date[0]) < int(from_date[0])) or (int(date[0]) > int(to_date[0])):
                        #day not within limit
                        continue

        # See iff any appointments met the criteria
        if len(appointments_list) != 0:
            message["msg"] = appointments_list
            return json.dumps(message)
        else:
            return '{"msg":"No appointments"}'

    def delete_staff_member(self,data):
        """Deletes a specific staff member by removing it from the data and returning it's information as a dict"""
        the_data = json.loads(data)
        index = 0
        for staff_member in self.__staff:
            if (the_data["staff_ssn"] == staff_member.get_staff()):
                return_msg = staff_member.get_staff_member()
                self.__staff.pop(index)
                return json.dumps(return_msg)
            index += 1
        else:
            return '{"msg":"No staff member with this ssn"}'


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
                if doctor.get_username() == data["username"]:
                    new_doctor = doctor.get_info()
                    message["msg"] = new_doctor
                    return json.dumps(message)     
            return '{"msg": "No Doctor Info"}'        
        except:
            return '{"msg": No Doctor Info"}'

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

    
    def delete_nurse(self, data):
        """
        Gets the username of a nurse to be deleted and deletes the nurse.
        """
        try:
            counter = 0
            for nurse in self.__nurses:
                nurse_name = nurse.get_username()
                if(data["username"] == nurse_name):
                    return_message = nurse.get_info()
                    self.__nurses.pop(counter)
                    return json.dumps(return_message)
            else:
                return '{"msg": "There is no nurse with this username"}'
        except:
            return '{ "msg": "It was unsuccessful at deleting the nurse." }'

