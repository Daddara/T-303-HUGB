PharmecyNames = {
    "1": "Apótek Hafnarfjarðar", 
    "2": "Lyf & heilsa Firði",
    "3": "Lyfja Setbergi"
}


PharmecyRequests = []

class Pharmecy:
  def __init__(self, pharmecy = None):
    self.pharmecy = PharmecyNames

  def get_all_pharmecy(self):
    return self.pharmecy

  def get_pharmecy(self, id):
    return self.pharmecy[id]
