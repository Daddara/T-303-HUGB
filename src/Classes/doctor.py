class Doctor:
    # username: string, name: string, email: string, note: string, department: string
    def __init__(self, username: str, name: str, email: str, note: str, department: str):
        self.__username = username
        self.__name = name
        self.__email = email
        self.__note = note
        self.__department = department
    
    def get_info(self):
        doctor_info_dict = {
            "username": self.__username,
            "name": self.__name,  
            "email": self.__email, 
            "note": self.__note,
            "department": self.__department
        }
        return doctor_info_dict
    
    def get_username(self):
        return self.__username

    def get_doctor_email(self):
        return self.__email

    def update_doctor(self, username, name, email, note, department):
        """Updates a patient and returns his info as a dictionary"""
        self.__username = username
        self.__name = name
        self.__email = email
        self.__note = note
        self.__department = department
        return self.get_doctor()


    def get_doctor(self):
        """Returns information about a patient in a dictionary"""
        doctor_dict = {
        "username": self.__username,
        "name": self.__name,
        "email" : self.__email,
        "note" : self.__note,
        "department": self.__department
        }
        return doctor_dict