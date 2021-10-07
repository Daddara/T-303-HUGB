class Nurse:
    # username: string, name: string, email: string, note: string
    def __init__(self, username: str, name: str, email: str, note: str):
        self.__username = username
        self.__name = name
        self.__email = email
        self.__note = note
    
    def get_info(self):
        nurse_info_dict = {
            "username": self.__username,
            "name": self.__name,  
            "email": self.__email, 
            "note": self.__note
        }
        return nurse_info_dict
    
    def get_username(self):
        return self.__username
    
    def get_nurse_email(self):
        return self.__email

    def update_nurse(self, username, name, email, note):
        """Updates a patient and returns his info as a dictionary"""
        self.__username = username
        self.__name = name
        self.__email = email
        self.__note = note
        return self.get_nurse()


    def get_nurse(self):
        """Returns information about a patient in a dictionary"""
        nurse_dict = {
        "username": self.__username,
        "name": self.__name,
        "email" : self.__email,
        "note" : self.__note
        }
        return nurse_dict