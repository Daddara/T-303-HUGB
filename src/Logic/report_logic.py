from copy import deepcopy
from tables import createTable

class ReportLogic():
    """Creates Pdf"""
    def generate_report(self, data, doctor_list, nurse_list, patient_list):
        """
        Generates a PDF report that list all doctors, nurses, and patients
        """
        # Deepcopy all data since in case there are some inadvertent changes
        doctor_data = deepcopy(doctor_list)
        nurse_data = deepcopy(nurse_list)
        patient_data = deepcopy(patient_list)

        table = createTable()
        # Changing a list of dicts to a list of lists
        doct_lis = table.list_of_d_to_list_of_l(doctor_data)
        nurse_lis = table.list_of_d_to_list_of_l(nurse_data)
        patient_lis = table.list_of_d_to_list_of_l(patient_data)

        # Getting the headers of all the tables
        p_header = table.create_header(patient_data)
        d_header = table.create_header(doctor_data)
        n_header = table.create_header(nurse_data)

        # Creating the tables for the PDF file
        table.create(doct_lis, d_header)
        table.create(nurse_lis, n_header)
        table.create(patient_lis, p_header)

        # This creates the PDF file
        table.final_pfd_creation()
    
        
        return("You have successfully created a PDF report document for the hospital")