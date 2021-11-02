import json
from data import Data
from Classes.appointment import Appointment

class TreatmentLogic():
    """contains all Logic and Dummydata for treatments"""
    def __init__(self):
        self.__data = Data()
        self.__treatment_prices = self.__data.get_treatment_prices()
        self.__appointments = self.__data.get_appointments()
    
    def get_treatment_database(self):
        """returns list of all treatments from the database"""
        return self.__treatment_prices
    
    def assign_treatment(self, data, patient_list, doctor_list):
        """Assigns an appointment to a patient"""
        data = json.loads(data)
        # See if the input patient exists
        patient_found = False
        for patient in patient_list:
            patient_username = patient.get_patient_id()
            if patient_username == data["patient_username"]:
                appointment_patient = patient_username
                patient_found = True

        if patient_found == False:
            return '{"Patient with this username does not exist"}'

        # See if the assigned doctor exist
        staff_involved = []
        for doctor in doctor_list:
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
            message = {}
            message["msg"] = new_appointment
            return json.dumps(message)
        except:
            return  '{"msg": "Creating this appointment was unsuccessful, please try again." }'
    
    def charge_for_service(self, data, patient_list):
        """Checks and creates the data needed for the receipt"""
        receipt_text = ""
        price = ""
        try:
            data = json.loads(data)

            # See if the input patient exists
            patient_found = False
            for patient in patient_list:
                patient_username = patient.get_patient_id()
                if patient_username == data["patient"]:
                    the_patient = patient_username
                    patient_found = True
                    break

            if patient_found == False:
                return '{"msg":"Patient with this username does not exist"}'

            
            if data["treatment"] == "1":
                receipt_text = "Checkup"
                price = (self.__treatment_prices["checkup"])
            elif data["treatment"] == "2":
                receipt_text = "Surgery"
                price = (self.__treatment_prices["surgery"])
            elif data["treatment"] == "3":
                receipt_text = "Catscan"
                price = (self.__treatment_prices["catscan"])
            elif data["treatment"] == "4":
                receipt_text = "X-rays"
                price = (self.__treatment_prices["xrays"])
            elif data["treatment"] == "5":
                receipt_text = "Bloodworks"
                price = (self.__treatment_prices["bloodworks"])
            elif data["treatment"] == "0":
                try:
                    price = int(data["price"])
                except:
                    return '{"msg":"Price needs to be on number format (no commas or dots either)"}'
                
                try:
                    receipt_text = (data["reason"])
                except:
                    return '{"msg":"Creating manual receipt unsuccessful"}'
            else:
                try:
                    treatment = int(data["treatment"])
                except:
                    return '{"msg":"Incorrect input when selecting reason for receipt"}'
                
                if treatment > 5 or treatment < 0:
                    return '{"msg":"Please select a number from the list for reason for receipt"}'

                return '{"msg":"Something wrong with input for reason of receipt"}'
                

            return_msg = {"patient": the_patient, "text": receipt_text, "price": price}
            message = {}
            message["msg"] = return_msg
            return json.dumps(message)
            
        except:   
            return '{"msg":"Unable to create receipt"}'