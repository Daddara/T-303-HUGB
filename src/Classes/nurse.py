class Nurse:
    """This class contains information about Nurses"""
    # username: string, name: string, email: string, note: string
    def __init__(self, username: str, name: str, email: str, note: str):
        self.__username = username
        self.__name = name
        self.__email = email
        self.__note = note
    
    def get_info(self):
        """Returns a nurse's information as a dictionary"""
        nurse_info_dict = {
            "username": self.__username,
            "name": self.__name,  
            "email": self.__email, 
            "note": self.__note
        }
        return nurse_info_dict
    
    def get_nurse_email(self):
        """Returns the email of a nurse"""
        return self.__email
    
    def get_username(self):
        """Returns the username of a nurse"""
        return self.__username

    def update_nurse(self, username, name, email, note):
        """Updates a nurse and returns their info as a dictionary"""
        self.__username = username
        self.__name = name
        self.__email = email
        self.__note = note
        return self.get_info()