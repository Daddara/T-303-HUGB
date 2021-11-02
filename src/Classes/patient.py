PRONOUN = {
    0: "Non Specific",
    1: "He",
    2: "She",
    3: "Zie",
    4: "Ey",
    5 : "Ve",
    6 : "Tey",
    7 : "E",
    8: "Name only"
}

class Patient:
  """This class keeps track of patients"""
  def __init__(self, p_username:str, p_name:str, p_email:str, p_note:str, p_doctor_id: str, p_nurse_id: str, p_pronoun=None):
    
    if p_pronoun == None:
        p_pronoun = PRONOUN[8]
    else:
        p_pronoun = PRONOUN[p_pronoun]
    
    self.__p_username = p_username
    self.__p_name = p_name
    self.p_email = p_email
    self.__p_note = p_note
    self.p_pronoun = p_pronoun
    self.p_doctor_id = p_doctor_id
    self.p_nurse_id = p_nurse_id

  def get_patient_id(self):
    """Returns the username of a patient, which is his id"""
    return self.__p_username

  def get_patient_email(self):
    """Returns the email of a patient"""
    return self.p_email

  def get_patient_name(self):
    """Returns the name of a patient"""
    return self.__p_name

  def update_patient(self, username, name, email, note, doctor_id):
    """Updates a patient and returns his info as a dictionary"""
    self.__p_username = username
    self.__p_name = name
    self.p_email = email
    self.__p_note = note
    self.p_doctor_id = doctor_id
    return self.get_patient()


  def get_patient(self):
    """Returns information about a patient in a dictionary"""
    patient_dict = {
      "username": self.__p_username,
      "name": self.__p_name,
      "email" : self.p_email,
      "note" : self.__p_note,
      "doctor_id" : self.p_doctor_id,
      "nurseid" : self.p_nurse_id,
      "pronoun": self.p_pronoun
    }
    return patient_dict

  def get_patient_records(self):
    """Specifically returns a patient's record."""
    return self.__p_note

