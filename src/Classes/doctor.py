class Doctor:
    """This class contains information about Doctors"""
    # username: string, name: string, email: string, note: string, department: string
    def __init__(self, username: str, name: str, email: str, note: str, department: str):
        self.__username = username
        self.__name = name
        self.__email = email
        self.__note = note
        self.__department = department
    
    def get_info(self):
        """Returns a doctor's information as a dictionary"""
        doctor_info_dict = {
            "username": self.__username,
            "name": self.__name,  
            "email": self.__email, 
            "note": self.__note,
            "department": self.__department
        }
        return doctor_info_dict
    
    def get_username(self):
        """Returns the username of a doctor"""
        return self.__username

    def get_doctor_email(self):
        """Returns the email of a doctor"""
        return self.__email

    def update_doctor(self, username, name, email, note, department):
        """Updates a doctor and returns their info as a dictionary"""
        self.__username = username
        self.__name = name
        self.__email = email
        self.__note = note
        self.__department = department
        return self.get_info()
