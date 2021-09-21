
class Patient:
  def __init__(self, p_ssn, p_name, p_address, p_phone, p_email, p_record):
    self.__p_ssn = p_ssn
    self.__p_name = p_name
    self.p_address = p_address
    self.p_phone = p_phone
    self.p_email = p_email
    self.__p_record = p_record


  def get_patient(self):
    patient_dict = {
      "ssn": self.__p_ssn,
      "name": self.__p_name,
      "address" : self.p_address,
      "phone" : self.p_phone,
      "email" : self.p_email,
      "record" : self.__p_record
    }
    return patient_dict

  def get_patient_records(self):
    return self.__p_record


if __name__ == "__main__":
  patient1 = Patient("1212889909", "Bjarni Benediktsson", "Akurbraut 17, 200", 8887122, "icehot@rikid.is", {})
  patient2 = Patient("3110659989", "Guðrún Högnadóttir", "Hvervisgata 30, 101", 6671129, "gudrun1@gmail.com", {"Allergies": ["lactose", "nut", "latex"], "Surgeries": ["hip surgery", "brain surgery"]})
  patient3 = Patient("0101059980", "Jón Gunnarsson", "Hamraborg 19, 201", 9910345, "jonniminn@tolfan.is", {"Medication": ["ritalin", "Parkodin", "Astma"]})
  patient_list = [patient1, patient2 , patient3]
  patient_id = ["1212889909", "3110659989", "0101059980"]
  counter = 0
  for patient in patient_list:
    print(patient.get_patient(patient_id[counter]))
    counter += 1