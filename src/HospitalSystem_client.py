# Autogenerated from websocket_client.template file
import asyncio
import websockets
import json
from os import system, name

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
    """Returns appointments which a specific staff member is assigned to"""
    staff_ssn = input("Enter your social security number(ssn): ")
    data = json.dumps({"staff_ssn":staff_ssn})
    return await send_msg("get_patient_appointments", data)


async def delete_patient():
    """Deletes a specific patient"""
    request = input("Please input patient id: ")
    patient_dict = {
        "patient_id": request,
    }
    return await send_msg("delete_patient", json.dumps(patient_dict))

async def send_presription ():
    """Creates a prescription"""
    try:
        request = input("Please input patient id, medicine name and pharmecy name with space inbetween words: ")
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
    patient_name = input("Please enter the patients full name: ")
    patient_email = input("Please enter the patients current email: ")
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
    doctor_name = input("Please enter the doctors full name: ")
    doctor_email = input("Please enter the doctors current email: ")
    doctor_username = ""
    data = {"name": doctor_name, "note": "", "email": doctor_email, "username": doctor_username
    }
    message = {"data": data}
    data = json.dumps(message)
    return await send_msg("create_doctor", message)



async def get_patient_list():
    """Lists all patients"""
    return await send_msg("get_patient_list", '{"doctor_id":"" }')


###Arnar

async def create_staff():
    staff_name = input("Please enter the staff member full name: ")
    staff_ssn = input("Please enter the staff member SSN: ")
    staff_address = input("Please enter the staff member address: ")
    staff_phone = input("Please enter the staff member phone: ")
    staff_title = input("Please enter the staff member title: ")
    data = {"name": staff_name, "ssn": staff_ssn, "address": staff_address, "phone": staff_phone,
     "title": staff_title}
    message = {"data": data}
    data = json.dumps(message)
    return await send_msg("create_staff", message)


#####


async def assign_treatment():
    """Assigns a patient to an appointment"""
    patient_username = input("Please enter the username of an existing patient: ")
    list_of_staff_ssn = input("Please enter the social security number of the overseer/doctor of the appointment: ")
    list_of_staff_ssn = list_of_staff_ssn.split(" ")
    print(list_of_staff_ssn)
    date = input("Please enter the date of the appointment. Write it in the format 'DD MM YYYY': ")
    date = date.split(" ")
    time = input("Please enter the set time of the appointment. Enter in format '00:00' : ")
    duration = input("Please enter the estimated duration of the appointment in minutes: ")
    print("Here are the available treatments:\n 1: Checkup\n2: Surgery\n3: Catscan\n4: x-rays\n5: Bloodworks")
    treatment = input("Please enter the number of the treatment for the appointment: ")
    description = input("Please enter the descpription of the appointment if there is one, otherwise press enter: ")
    data = {"patient_username": patient_username, "staff": list_of_staff_ssn, "date": date, "time": time, "duration": duration, "treatment":treatment, "description": description}
    data = json.dumps(data)
    return await send_msg("assign_treatment", data)

async def delete_staff_member():
    """Deletes a specific staff member"""
    request = input("Please input staff member's social security number: ")
    staff_dict = {
        "staff_ssn": request,
    }
    return await send_msg("delete_staff_member", json.dumps(staff_dict))


if __name__ == "__main__":
    # Call each of the generated webSocket methods once and await results.
    print("\t\tWelcome to the Hospital System\n")
    menu = "\n\
            Enter 1 to create a new patient for the system\n\
            Enter 2 to get a patients info\n\
            Enter 3 to list all appointments for a doctor\n\
            Enter 4 to assign a treatment to a patient \n\
            Enter 5 to send a prescription to a patient\n\
            Enter 6 to delete a patient\n\
            Enter 7 to delete a staff member\n\
            Enter 8 to add a staff member\n\
            Enter q to quit\n\
            "
    while True:
        print(menu)
        user_input = input("Please enter your selection here: ")
        if user_input == "q" or user_input == "Q":
            break
        elif user_input == "1":
            print(asyncio.run(create_patient()))
        elif user_input == "2":
            print(asyncio.run(get_patient_info()))
        elif user_input == "3":
            print(asyncio.run(get_patient_appointments()))
        elif user_input == "4":
            print(asyncio.run(assign_treatment()))
        elif user_input == "5":
            print(asyncio.run(send_presription()))
        elif user_input == "6":
            print(asyncio.run(delete_patient()))
        elif user_input == "7":
            print(asyncio.run(delete_staff_member()))
        elif user_input == "8":
            print(asyncio.run(create_staff()))
        else:
            print("Please enter a valid number")
    
    
    
    
    # print(asyncio.run( assign_treatment()))
    # print(asyncio.run(get_patient_list()))