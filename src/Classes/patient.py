class Patient:
  def __init__(self, p_username:str, p_name:str, p_email:str, p_note:str, p_doctor_id: str, p_nurse_id: str):
    self.__p_username = p_username
    self.__p_name = p_name
    self.p_email = p_email
    self.__p_note = p_note
    self.p_doctor_id = p_doctor_id
    self.p_nurse_id = p_nurse_id

  def get_patient_id(self):
    return self.__p_username

  def get_patient_name(self):
    return self.__p_name


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


# if __name__ == "__main__":
#   patient1 = Patient("1212889909", "Bjarni Benediktsson", "Akurbraut 17, 200", 8887122, "icehot@rikid.is", {})
#   patient2 = Patient("3110659989", "Guðrún Högnadóttir", "Hvervisgata 30, 101", 6671129, "gudrun1@gmail.com", {"Allergies": ["lactose", "nut", "latex"], "Surgeries": ["hip surgery", "brain surgery"]})
#   patient3 = Patient("0101059980", "Jón Gunnarsson", "Hamraborg 19, 201", 9910345, "jonniminn@tolfan.is", {"Medication": ["ritalin", "Parkodin", "Astma"]})
#   patient_list = [patient1, patient2 , patient3]
#   patient_id = ["1212889909", "3110659989", "0101059980"]
#   counter = 0
#   for patient in patient_list:
#     print(patient.get_patient(patient_id[counter]))
#     counter += 1
