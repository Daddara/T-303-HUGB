patientRecords = {
    "1": ["Sara" , "23"],
    "2": ["Daniel", "21"]
}




class Patients:
  def __init__(self, patients = None):
    self.patients = patientRecords

  def get_all_patients(self):
    return self.patients

  def get_patient(self, id):
    return self.patients[id]
