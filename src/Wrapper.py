from data import Data
from Logic.patient_logic import PatientLogic
from Logic.doctor_logic import DoctorLogic
from Logic.nurse_logic import NurseLogic
from Logic.staff_logic import StaffLogic
from Logic.prescription_logic import PrescriptionLogic
from Logic.appointment_logic import AppointmentLogic
from Logic.treatment_logic import TreatmentLogic
from Logic.report_logic import ReportLogic



class Wrapper:
    '''Used as a subroutine between logics'''
    def __init__(self):
        self.__patient_logic = PatientLogic()
        self.__doctor_logic = DoctorLogic()
        self.__nurse_logic = NurseLogic()
        self.__staff_logic = StaffLogic()
        self.__prescription_logic = PrescriptionLogic()
        self.__appointment_logic = AppointmentLogic()
        self.__treatment_logic = TreatmentLogic()
        self.__report_logic = ReportLogic()


    #### PATIENT METHODS ####

    def update_patient(self, data):
        """Updates information about an existing patient."""
        return self.__patient_logic.update_patient(data)
        
    def get_patient_list(self):
        """Returns all patients' info as dictionaries"""
        return self.__patient_logic.get_patient_list()

    def create_patient(self, data):
        """Takes a json object and turns into a dictionary that is then passed
            to create a Patient object with the data. Returns a json value"""
        return self.__patient_logic.create_patient(data)
        
    def get_patient_info(self, data):
        """Returns a patient's information as a dictionary if it exists in the system"""
        return self.__patient_logic.get_patient_info(data)

    def delete_patient(self,data):
        """Deletes a patient with a particular username"""
        return self.__patient_logic.delete_patient(data)

    def get_medical_history(self, data):
        """Returns a patients medical history if he has any"""
        return self.__patient_logic.get_medical_history(data)

    #### DOCTOR METHODS ####

    def create_doctor(self, data):
        """Takes a json object and turns into a dictionary that is then passed
            to create a Patient object with the data. Returns a json value"""
        return self.__doctor_logic.create_doctor(data)

    def get_doctors_list(self):
        """Returns a list of all doctors"""
        return self.__doctor_logic.get_doctors_list()

    def get_doctor(self, data):
        """returns doctor if it is in the system"""
        return self.__doctor_logic.get_doctor(data)
    
    def delete_doctor(self, data):
        """Deletes a doctor with a particular username"""
        return self.__doctor_logic.delete_doctor(data)

    def update_doctor (self, data):
        """Updates information about an existing doctor."""
        return self.__doctor_logic.update_doctor(data)

    #### NURSE METHODS ####

    def create_nurse(self, data):
        """Creates a new instance of a Nurse"""
        return self.__nurse_logic.create_nurse(data)  

    def get_nurses_list(self):
        """Returns a list of all nurses"""
        return self.__nurse_logic.get_nurses_list()

    def get_nurse(self, data):
        """Prints out nurse if it is in the system"""
        return self.__nurse_logic.get_nurse(data)

    def update_nurse(self, data):
        """Updates information about an existing nurse."""
        return self.__nurse_logic.update_nurse(data)
    
    def delete_nurse(self, data):
        """Gets the username of a nurse to be deleted and deletes the nurse."""
        return self.__nurse_logic.delete_nurse(data)

    #### STAFF METHODS ####

    def create_staff(self, data):
        """Takes a json object and turns into a dictionary that is then passed
            to create a staff object with the data. Returns a json value"""
        return self.__staff_logic.create_staff(data)
    
    def delete_staff_member(self,data):
        """Deletes a specific staff member by removing it from the data and returning it's information as a dict"""
        return self.__staff_logic.delete_staff_member(data)


    #### OTHER METHODS ####

    def send_presription(self, data):
        ''' This function takes in name of medicine and pharmecy along with the id of a patient.
        The function uses it to send a prescription for the medicine to the pharmecy for the patient. 
        As of now, you can only prescribe existing patients with Ibufen or Parcodine, at either 
        the Apótekið or Heilsuver'''
        patient_list = self.__patient_logic.get_patient_database()
        return self.__prescription_logic.send_presription(data, patient_list)

    

    def assign_treatment(self, data):
        """Assigns an appointment to a patient"""
        patient_list = self.__patient_logic.get_patient_database()
        doctor_list = self.__doctor_logic.get_doctor_database()
        return self.__treatment_logic.assign_treatment(data, patient_list, doctor_list)    

    def get_appointments(self, data):
        """Returns a list of appointments that a doctor is assigned to"""
        return self.__appointment_logic.get_appointments(data)

    def get_appointments_at_date(self, data):
        """
        Returns all appointments as a dictionary if they belong to the inserted doctor
        and if the date of the appointment is within searching range
        """
        doctor_list = self.__doctor_logic.get_doctor_database()
        return self.__appointment_logic.get_appointments_at_date(data, doctor_list)

    def charge_for_service(self, data):
        """Checks and creates the data needed for the receipt"""
        patient_list = self.__patient_logic.get_patient_database()
        return self.__treatment_logic.charge_for_service(data, patient_list)


    def generate_report(self, data):
        """
        Generates a PDF report that list all doctors, nurses, and patients
        """
        patient_list = self.__patient_logic.get_patient_database()
        doctor_list = self.__doctor_logic.get_doctor_database()
        nurse_list = self.__nurse_logic.get_nurse_database()
        return self.__report_logic.generate_report(data, doctor_list, nurse_list, patient_list)