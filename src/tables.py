
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
        self.__fileName = 'report.pdf'
        self.__pdf = canvas.Canvas("report.pdf")
        self.__pdf.setTitle("Report")
        self.__pdf = SimpleDocTemplate(
            self.__fileName,
            pagesize=landscape(letter),
            showBoundary=0
        )
        self.__elems = []

    def create(self, data: list, header):
        
        

        table = Table(data)

        # add style

        style = TableStyle([
            ('BACKGROUND', (0,0), (len(data)+1,0), colors.green),
            ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),

            ('ALIGN',(0,0),(-1,-1),'CENTER'),

            ('FONTSIZE', (0,0), (-1,0), 14),

            ('BOTTOMPADDING', (0,0), (-1,0), 12),

            ('BACKGROUND',(0,1),(-1,-1),colors.lightsteelblue),
        ])
        table.setStyle(style)

        # 2) Alternate backgroud color
        rowNumb = len(data)
        for i in range(1, rowNumb):
            if i % 2 == 0:
                bc = colors.burlywood
            else:
                bc = colors.beige
            
            ts = TableStyle(
                [('BACKGROUND', (0,i),(-1,i), bc)]
            )
            table.setStyle(ts)

        # 3) Add borders
        ts = TableStyle(
            [
            ('BOX',(0,0),(-1,-1),2,colors.black),

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
        styles = getSampleStyleSheet()
        title_style = styles['Heading1']
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
        self.__pdf.build(self.__elems)


    def get_keys(self, data):
        ret_list = []
        try:  
            if isinstance(data[0], Patient):
                    ret_list.append(list(data[0].get_patient().keys()))
            elif isinstance(data[0], Doctor) or isinstance(data[0], Nurse):
                    ret_list.append(list(data[0].get_info().keys()))
        except:
            print("There is no data to be read here.")
        return ret_list

    def list_of_d_to_list_of_l(self, data):
        ret_list = self.get_keys(data)
        for items in data:
            if isinstance(items, Patient):
                some_dict = items.get_patient()
            elif isinstance(items, Doctor) or isinstance(items, Nurse):
                some_dict = items.get_info()
            ret_list.append(list(some_dict.values()))
        return ret_list


if __name__ == "__main__":
    main_data = Data()
    patient_data =main_data.get_patients()
    doctor_data =main_data.get_doctors()
    nurse_data = main_data.get_nurses()
    table = createTable()
    new_list_data = table.list_of_d_to_list_of_l(patient_data)
    doct_lis = table.list_of_d_to_list_of_l(doctor_data)
    nurse_lis = table.list_of_d_to_list_of_l(nurse_data)
    p_header = table.create_header(patient_data)
    d_header = table.create_header(doctor_data)
    n_header = table.create_header(nurse_data)
    table.create(doct_lis, d_header)
    table.create(nurse_lis, n_header)
    table.create(new_list_data, p_header)
    table.final_pfd_creation()
    