class Staff():
    """Keep track of staff members"""
    def __init__(self, s_name:str, s_ssn:str, s_title:str, s_address=None, s_phone=None):
        self.__s_name = s_name
        self.__s_ssn = s_ssn
        self.__s_title = s_title
        self.__s_address = s_address
        self.__s_phone = s_phone

    def get_staff_member(self):
        ''' Searches for staff member on ssn and then returns json of all it's attributes'''
        staff_dict = {
            "name": self.__s_name,
            "ssn": self.__s_ssn,  
            "address": self.__s_address, 
            "phone": self.__s_phone, 
            "title": self.__s_title,
        }
        return staff_dict
    
    def get_staff(self):
        """Returns the social security number of a staff member"""
        return self.__s_ssn

    def get_staff_name(self):
        """Returns the name of a staff member"""
        return self.__s_name
