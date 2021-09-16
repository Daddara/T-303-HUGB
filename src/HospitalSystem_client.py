# Autogenerated from websocket_client.template file
import asyncio
import websockets
import json

opperations = {"1": "Surgery", "2": "Cat scan"}

# This method just sends an arbitrary webSocket message in 'our' format (op and data)
async def send_msg(op, data):
    uri = "ws://127.0.0.1:8080"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"op": op, "data": data}))

        return_val = await websocket.recv()
        # Also, instead of printing the result we return it
        return return_val


async def get_patient_info():
    return await send_msg("get_patient_info", "{ }")


async def get_patient_appointments():
    return await send_msg("get_patient_appointments", '{"doctor_id":"" }')


async def delete_patient():
    return await send_msg("delete_patient", '{"patient_id":"" }')


async def send_presription():
    request = input(
        "Please input patient id, Medicine id and pharmecy id with space inbetween "
    )
    data = list(request)
    return await send_msg("send_presription", data)


async def create_patient():
    return await send_msg("create_patient", '{"patient_data":"" }')


async def get_patient_list():
    return await send_msg("get_patient_list", '{"doctor_id":"" }')


async def assign_opperation():

    return await send_msg("assign_opperation", "{'doctor_id':'' }")


if __name__ == "__main__":
    # Call each of the generated webSocket methods once and await results.
    print(asyncio.run(get_patient_info()))
    print(asyncio.run(get_patient_appointments()))
    print(asyncio.run(delete_patient()))
    print(asyncio.run(send_presription()))
    # print(asyncio.run(create_patient()))
    # print(asyncio.run(get_patient_list()))
