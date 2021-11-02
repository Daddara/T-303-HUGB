
from reportlab.lib import colors
from reportlab.lib.pagesizes import A2, landscape, letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.platypus.flowables import Spacer

from Classes.doctor import Doctor
from Classes.nurse import Nurse
from Classes.patient import Patient
from data import Data


class createTable:
    def __init__(self) -> None:
        '''Initializes the PDF report by creating the filename as well as a title
         and some margins to where our tables are created.'''
        style = getSampleStyleSheet()
        title_style = style['Heading1']
        title_style.alignment = 1
        self.__fileName = 'HospitalReport.pdf'
        self.__pdf = SimpleDocTemplate(
            self.__fileName,
            pagesize=letter,
            title="Hospital Report",
            showBoundary=0,
            _pageBreakQuick=1,
            leftMargin=5,
            rightMargin=5,
            topMargin=50,
            bottomMargin=50
            
        )
        self.__elems = [Paragraph("Hospital Report", title_style)]

    def create(self, data: list, header):
        '''This is where the tables are created, with the first row being unique.
        The first row is the first list in the list of lists, being the keys in the dicts.
        The first row is styled differently as well.'''
        

        table = Table(data)

        style = TableStyle([
            ('BACKGROUND', (0,0), (len(data[0])+1,0), colors.green),
            ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),

            ('ALIGN',(0,0),(-1,-1),'CENTER'),

            ('FONTSIZE', (0,0), (-1,0), 12),

            ('BOTTOMPADDING', (0,0), (-1,0), 12),

            ('BACKGROUND',(0,1),(-1,-1),colors.black),
        ])
        table.setStyle(style)

        # 2) Alternate backgroud color
        rowNumb = len(data)
        for i in range(1, rowNumb):
            if i % 2 == 0:
                bc = colors.burlywood
            else:
                bc = colors.white
            
            ts = TableStyle(
                [('BACKGROUND', (0,i),(-1,i), bc)]
            )
            table.setStyle(ts)

        # 3) Add borders
        ts = TableStyle(
            [
            ('BOX',(0,0),(-1,-1),2,colors.black),
            ('FONTSIZE', (0,1), (-1,-1), 10),
            ('ALIGN',(0,1),(-1,-1),'CENTER'),
            ('LINEBEFORE',(2,1),(2,-1),2,colors.red),
            ('LINEABOVE',(0,2),(-1,2),2,colors.green),

            ('GRID',(0,0),(-1,-1),2,colors.black),
            ]
        )
        table.setStyle(ts)
        s = Spacer(width=0, height=25)
        self.__elems.append(header)
        self.__elems.append(table)
        self.__elems.append(s)
        

    def create_header(self, data):
        '''Creates a header for the table, with unique headers for the classes.
        Open for extension'''
        styles = getSampleStyleSheet()
        title_style = styles['Heading2']
        title_style.alignment = 1
        
        if isinstance(data[0], Patient):
            if len(data) > 1:
                title = Paragraph("Patients", title_style)
            else:
                title = Paragraph("Patient", title_style)
        elif isinstance(data[0], Doctor):
            if len(data) > 1:
                title = Paragraph("Doctors", title_style)
            else:
                title = Paragraph("Doctor", title_style)
        elif isinstance(data[0], Nurse):
            if len(data) > 1:
                title = Paragraph("Nurses", title_style)
            else:
                title = Paragraph("Nurse", title_style)
        return title

    def final_pfd_creation(self):
        '''This is where we add all the headers and tables together.'''
        self.__pdf.build(self.__elems)


    def get_keys(self, data):
        '''Capitalizes and gets all the keys from the dictionaries.'''
        ret_list = []
        try:  
            if isinstance(data[0], Patient):
                    ret_list.append(list(data[0].get_patient().keys()))
            elif isinstance(data[0], Doctor) or isinstance(data[0], Nurse):
                    ret_list.append(list(data[0].get_info().keys()))
        except:
            print("There is no data to be read here.")
        ret_list[0] = [context.capitalize() for context in ret_list[0]]
        return ret_list

    def list_of_d_to_list_of_l(self, data):
        '''Converts the list of dictionaries to a list of lists for the PDF generator'''
        ret_list = self.get_keys(data)
        for items in data:
            if isinstance(items, Patient):
                some_dict = items.get_patient()
            elif isinstance(items, Doctor) or isinstance(items, Nurse):
                some_dict = items.get_info()
            ret_list.append(list(some_dict.values()))
        if isinstance(data[0], Patient):
            ret_list = self.make_para_notes_patient(ret_list)
        return ret_list


    def make_para_notes_patient(self, data):
        '''Edits the notes in patient to better fit the PDF page.'''
        styles = getSampleStyleSheet()
        counter = 0
        for patient in data:
            if counter > 0:
                patient[3] = Paragraph(patient[3], styles['Normal'])
            counter += 1
        return data

if __name__ == "__main__":
    main_data = Data()
    patient_data =main_data.get_patients()
    doctor_data =main_data.get_doctors()
    nurse_data = main_data.get_nurses()
    table = createTable()
    new_list_data = table.list_of_d_to_list_of_l(patient_data)
    # doct_lis = table.list_of_d_to_list_of_l(doctor_data)
    # nurse_lis = table.list_of_d_to_list_of_l(nurse_data)
    p_header = table.create_header(patient_data)
    # d_header = table.create_header(doctor_data)
    # n_header = table.create_header(nurse_data)
    # table.create(doct_lis, d_header)
    # table.create(nurse_lis, n_header)
    table.create(new_list_data, p_header)

    table.final_pfd_creation()
    