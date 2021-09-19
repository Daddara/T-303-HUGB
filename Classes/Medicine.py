MedicineNames = {
    "1": ["Ibufen"],
    "2": ["Sýklalyf"]
}


class Medicine:
  def __init__(self, medicine = None):
    self.medicine = MedicineNames

  def get_all_medicine(self):
    return self.medicine

  def get_medicine(self, id):
    return self.medicine[id]
