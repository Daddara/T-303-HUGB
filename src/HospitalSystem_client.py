# Autogenerated from websocket_client.template file
import asyncio
import websockets
import json
import getpass
from dotenv import load_dotenv
import os
from os import error, system, name
from passlib.context import CryptContext

from Classes.prescription import Prescription

# This method just sends an arbitrary webSocket message in 'our' format (op and data)
async def send_msg(op, data):
    uri = "ws://127.0.0.1:8888"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"op": op, "data": data}))

        return_val = await websocket.recv()
        # Also, instead of printing the result we return it
        return return_val


async def get_patient_info():
    """Returns a dictionary of a patient's info"""
    try:
        request = input("Please input patient username: ")
        return await send_msg("get_patient_info", request)
    except:
        return {"msg":"Please enter a valid patient username."}


async def get_patient_appointments():
    """Returns appointments which a specific doctor is assigned to"""
    username = input("Enter a doctor's username: ")
    data = json.dumps({"username":username})
    return await send_msg("get_patient_appointments", data)

async def get_appointments_at_date():
    """Returns all appointments that a doctor has for a specific period"""
    doctor_username = input("Please enter username for a doctor: ")
    first_date = input("Enter from date on the format DD MM YYYY, separated by space: ")
    first_date = first_date.split(" ")
    second_date = input("Enter to date on the format DD MM YYYY, separated by space: ")
    second_date = second_date.split(" ")
    data = json.dumps({"doctor": doctor_username, "from_date": first_date, "to_date": second_date})
    return await send_msg("get_appointments_at_date", data)


async def delete_patient():
    """Deletes a specific patient"""
    request = input("Please input patient username: ")
    patient_dict = {
        "patient_id": request,
    }
    return await send_msg("delete_patient", json.dumps(patient_dict))

async def delete_nurse():
    username = input("Please input a nurse's username: ")
    nurse_dict = {"username": username}
    return await send_msg("delete_nurse", json.dumps(nurse_dict))

async def send_presription ():
    """Creates a prescription"""
    try:
        request = input("Please input medicine name, pharmecy name and patient id with space inbetween words: ")
        data = request.split()
        json_data = {
                "medicine": data[0],
                "pharmecy": data[1],
                "patient_id": data[2]

            }
        return await send_msg("send_presription", json.dumps(json_data))
    except:
        return '{"msg": "Not valid input"}'

async def create_patient():
    """Creates a new patient"""
    patient_name = input("Please enter the patient's full name: ")
    patient_email = input("Please enter the patient's current email: ")
    patient_note = ""
    patient_note = input("Please enter any patient notes: ")
    patient_username = ""
    data = {"username": patient_username, "name": patient_name, "email": patient_email,
     "note": patient_note, "doctorid": "", "nurseid": ""}
    message = {"data": data}
    data = json.dumps(message)
    return await send_msg("create_patient", message)

async def create_doctor():
    """Creates a new doctor"""
    doctor_name = input("Please enter the doctor's full name: ")
    doctor_email = input("Please enter the doctor's current email: ")
    doctor_username = ""
    data = {"name": doctor_name, "note": "", "email": doctor_email, "username": doctor_username
    }
    message = {"data": data}
    data = json.dumps(message)
    return await send_msg("create_doctor", message)

async def get_patient_list():
    """Lists all patients"""
    return await send_msg("get_patient_list", '{"doctor_id":"" }')

async def create_staff():
    """Creates a new staff member"""
    staff_name = input("Please enter the staff member full name: ")
    staff_ssn = input("Please enter the staff member Social Security Number: ")
    staff_address = input("Please enter the staff member address: ")
    staff_phone = input("Please enter the staff member phone: ")
    staff_title = input("Please enter the staff member title: ")
    data = {"name": staff_name, "ssn": staff_ssn, "address": staff_address, "phone": staff_phone,
     "title": staff_title}
    message = {"data": data}
    data = json.dumps(message)
    return await send_msg("create_staff", message)

async def create_nurse():
    """Creates a new nurse"""
    nurse_name = input("Please enter full name: ")
    nurse_email = input("Please enter email: ")
    nurse_note = ""
    nurse_note = input("Please enter any nurse's notes: ")
    nurse_username = ""
    data = {"username": nurse_username, "name": nurse_name, "email": nurse_email,
     "note": nurse_note}
    message = {"data": data}
    data = json.dumps(message)
    return await send_msg("create_nurse", message)


async def assign_treatment():
    """Assigns a patient to an appointment"""
    patient_username = input("Please enter the username of an existing patient: ")
    doctor = input("Please enter the username of the overseer/doctor of the appointment: ")
    list_of_staff = [] 
    list_of_staff.append(doctor)
    date = input("Please enter the date of the appointment. Write it in the format 'DD MM YYYY': ")
    date = date.split(" ")
    time = input("Please enter the set time of the appointment. Enter in format '00:00' : ")
    duration = input("Please enter the estimated duration of the appointment in minutes: ")
    print("Here are the available treatments:\n1: Checkup\n2: Surgery\n3: Catscan\n4: x-rays\n5: Bloodworks")
    treatment = input("Please enter the number of the treatment for the appointment: ")
    description = input("Please enter the descpription of the appointment if there is one, otherwise press enter: ")
    data = {"patient_username": patient_username, "staff": list_of_staff, "date": date, "time": time, "duration": duration, "treatment":treatment, "description": description}
    data = json.dumps(data)
    return await send_msg("assign_treatment", data)

async def delete_staff_member():
    """Deletes a specific staff member"""
    request = input("Please input staff member's social security number: ")
    staff_dict = {
        "staff_ssn": request,
    }
    return await send_msg("delete_staff_member", json.dumps(staff_dict))


async def generate_report():
    try:
        context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=50000
)
        count = 1
        while count <= 3:
            print("Please enter your credentials:")
            admin_username = input("Username: ")
            admin_password = getpass.getpass()
            # adm1 = context.hash("admin")
            # adm2 = context.hash("admin")
            # print(adm1 + adm2)
            f = open('data.json',)
            data = json.load(f)
            adm1 = data["username"]
            adm2 = data["password"]
            if context.verify(admin_username, adm1) and context.verify(admin_password, adm2):
                return await send_msg("generate_report", admin_username)
            else:
                print("Wrong credentials entered")
            count += 1
        print("Too many failed attempts")
    except Exception as error:
        print(error)
    

## If this file is run, the user can test the functionalities that have been implemented
## These are only the functions that are not covered by the frontend

if __name__ == "__main__":
    # Call each of the generated webSocket methods once and await results.
    print("\t\tWelcome to the Hospital System\n")
    menu = "\n\
            Enter 1 to list all appointments a doctor has\n\
            Enter 2 to assign a treatment to a patient \n\
            Enter 3 to create a prescription for a patient\n\
            Enter 4 to delete a staff member\n\
            Enter 5 to add a staff member\n\
            Enter 6 to list all appointments a doctor has for a certain time period\n\
            Enter 7 to generate a report as an administrator \n\
            Enter q to quit\n\
            "
    while True:
        print(menu)
        user_input = input("Please enter your selection here: ")
        if user_input == "q" or user_input == "Q":
            break
        elif user_input == "1":
            print(asyncio.run(get_patient_appointments()))
        elif user_input == "2":
            print(asyncio.run(assign_treatment()))
        elif user_input == "3":
            newPrescription = asyncio.run(send_presription())
            theData = json.loads(newPrescription)
            print("The medicine: " + theData["medicine"] + " has been sent to the pharmecy: " + theData["pharmecy"] + " for the patient: " + theData["patient_id"])
        elif user_input == "4":
            print(asyncio.run(delete_staff_member()))
        elif user_input == "5":
            print(asyncio.run(create_staff()))
        elif user_input == "6":
            print(asyncio.run(get_appointments_at_date()))
        elif user_input == "7":
            print(asyncio.run(generate_report()))
        else:
            print("Please enter a valid number")
    
