# Autogenerated from websocket_client.template file
import asyncio
import websockets
import json
from os import system, name

# This method just sends an arbitrary webSocket message in 'our' format (op and data)
async def send_msg(op, data):
    uri = "ws://127.0.0.1:8080"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"op": op, "data": data}))

        return_val = await websocket.recv()
        # Also, instead of printing the result we return it
        return return_val


async def get_patient_info():
    request = input("Please input patient id: ")
    patient_dict = {
        "patient_id": request,
    }
    return await send_msg("get_patient_info", json.dumps(patient_dict))


async def get_patient_appointments():
    staff_ssn = input("Enter your social security number(ssn): ")
    data = json.dumps({"staff_ssn":staff_ssn})
    return await send_msg("get_patient_appointments", data)


async def delete_patient():
    return await send_msg("delete_patient", '{"patient_id":"" }')

async def send_presription ():
    request = input("Please input patient id, medicine name and pharmecy name with space inbetween words: ")
    data = request.split()
    json_data = {
            "medicine": data[0],
            "pharmecy": data[1],
            "patient_id": data[2]

        }
    return await send_msg("send_presription", json.dumps(json_data))


async def create_patient():
    patient_ssn = input("Please enter the patients social security number: ")
    patient_name = input("Please enter the patients full name: ")
    patient_address = input("Please enter the patients current address: ")
    patient_phone = input("Please enter the patients current phone number: ")
    patient_email = input("Please enter the patients current email: ")
    patient_record = {}
    data = {"ssn": patient_ssn, "name": patient_name, "address": patient_address, 
    "phone": patient_phone, "email": patient_email, "record": patient_record}
    data = json.dumps(data)
    return await send_msg("create_patient", data)


async def get_patient_list():
    return await send_msg("get_patient_list", '{""}')


async def assign_treatment():
    return await send_msg("assign_opperation", "{'doctor_id':'' }")


if __name__ == "__main__":
    # Call each of the generated webSocket methods once and await results.
    print("\t\tWelcome to the Hospital System\n")
    menu = "\n\
            Enter 1 to create a new patient for the system\n\
            Enter 2 to get a patients info\n\
            Enter 3 to list all patients\n\
            Enter 4 to list all appointments for a doctor\n\
            Enter 5 to assign a treatment to a patient \n\
            Enter 6 to send a prescription to a patient\n\
            Enter 7 to delete a patient\n\
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
            print(asyncio.run(get_patient_list()))
        elif user_input == "4":
            print(asyncio.run(get_patient_appointments()))
        elif user_input == "5":
            print(asyncio.run( assign_treatment()))
        elif user_input == "6":
            print(asyncio.run(send_presription()))
        elif user_input == "7":
            print(asyncio.run(delete_patient()))
        else:
            print("Please enter a valid number")
    
    
    
    
    # print(asyncio.run( assign_treatment()))
    # print(asyncio.run(get_patient_list()))
