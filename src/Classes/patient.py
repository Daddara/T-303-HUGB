class Patient:
  """This class keeps track of patients"""
  def __init__(self, p_username:str, p_name:str, p_email:str, p_note:str, p_doctor_id: str, p_nurse_id: str):
    self.__p_username = p_username
    self.__p_name = p_name
    self.p_email = p_email
    self.__p_note = p_note
    self.p_doctor_id = p_doctor_id
    self.p_nurse_id = p_nurse_id

  def get_patient_id(self):
    """Returns the id for a patient, which is his username"""
    return self.__p_username

  def get_patient_email(self):
    return self.p_email

  def get_patient_name(self):
    """Returns the name of a patient"""
    return self.__p_name

  def update_patient(self, username, name, email, note):
    """Updates a patient and returns his info as a dictionary"""
    self.__p_username = username
    self.__p_name = name
    self.p_email = email
    self.__p_note = note
    return self.get_patient()


  def get_patient(self):
    """Returns information about a patient in a dictionary"""
    patient_dict = {
      "username": self.__p_username,
      "name": self.__p_name,
      "email" : self.p_email,
      "note" : self.__p_note,
      "doctorid" : self.p_doctor_id,
      "nurseid" : self.p_nurse_id
    }
    return patient_dict

  def get_patient_records(self):
    """Specifically returns a patient's record."""
    return self.__p_note

