from data import Data
import json
from Classes.appointment import Appointment

class AppointmentLogic():
    def __init__(self):
        self.__data = Data()
        self.__appointments = self.__data.get_appointments()
    
    def get_appointment_database(self):
        return self.__appointments
    
    def get_appointments(self, data):
        """Returns a list of appointments that a doctor is assigned to"""
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
            return '{"msg":"Missing arguments: username"}'

    def get_appointments_at_date(self, data, doctor_list):
        """
        Returns all appointments as a dictionary if they belong to the inserted doctor
        and if the date of the appointment is within searching range
        """
        data = json.loads(data)

        # Check if the username belongs to a doctor in the database
        doctor_found = False
        for doctor in doctor_list:
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