# Interface Description Hospital Frontend #

## Version ##
Current version: s4\_2\_0

Date: 1st October 2021

## Change log ##
- s3\_1\_0: Initial version, Sprint 3.
- s4\_2\_0: Sprint 4 version. Added doctors and nurses, and option to change doctor when updating patients. Readme, examples, and interface files have been updated accordingly.
- s4\_2\_1: Added the individual read methods that were forgotten before (`read_patient`, `read_doctor`, `read_nurse`).

## Protocol ##
The frontend communicates in a client-server fashion with the backend, where the frontend is the client. That means the backend only answers, and never sends messages independently to the frontend.

1. For each message, the frontend establishes a new connection, sends the message, and closes the connection after receiving the message. This is already supported by the example code covered in the lectures and by the interface generator.
2. A correct message from the frontend to the backend is a JSON object that contains both a field called **op** and a field called **data**. Additional fields can be ignored. The backend needs to be robust to wrongly-formatted messages (i.e., it shouldn not crash if something else is sent). An example for a correctly-formatted message would be: `{"op":"readAll_patient", "data": {}}`, attempting to call the operation **readAll_patient** with no input parameters.
3. The data field in the input message contains all input parameters, following the names listed below. For instance, a correct call to **delete_patient** would need to have a string attribute called **username** in the data part of the message.
4. The backend always returns a JSON object.

In case of success, the JSON object contains a single attribute called **msg**. The msg field contains a JSON object according to the relevant output/return parameters of the operation. The output parameters are discussed below. For example, a successful call to **create_patient** returns an object that contains all the patient's attributes. 

In case of an error, the server returns a JSON object with a single attribute **error**, containing the error message as a string.

The backend should make sure to return all of the required parameters, as the frontend might not be robust to wrong entities or data types.

## Supported Operations ##
The following operations are currently supported. Note that the data model is described further down.

| Operation name | Input parameters | Output/return parameters | Description |
| ----------- | ----------- | ----------- | ----------- |
| **readAll_patient** | None | [Patient] | Returns an array of all existing patients in the system. If no patient exists, an empty array is returned. |
| **create_patient** | name:String, note:String, email:String, username:String | Patient | Creates a patient with the provided parameters. The username has to be unique. If successful, returns the created patient object. `doctor_id` and `nurse_id` are expected to be **null** on creation. |
| **update_patient** | name:String, note:String, email:String, username:String, doctor\_id: String, nurse\_id: String | Patient | Updates the patient with the provided username according to the provided parameters. If successful, returns the updated patient object. Currently, the frontend always provides a null value for `nurse_id`.|
| **delete_patient** | username:String | Patient | Deletes the patient with the provided username. If successful, returns the deleted patient object. |
| **read_patient** | username:String | Patient | Returns the patient with the provided username. Returns an error if the patient does not exist. |
| ----------- | ----------- | ----------- | ----------- |
| **readAll_doctor** | None | [Doctor] | Returns an array of all existing doctors in the system. If no doctor exists, an empty array is returned. |
| **create_doctor** | name:String, note:String, email:String, username:String | Doctor | Creates a doctor with the provided parameters. The username has to be unique. If successful, returns the created doctor object. The department is expected to be null on creation. |
| **update_doctor** | name:String, note:String, email:String, username:String, department: String | Doctor | Updates the doctor with the provided username according to the provided parameters. If successful, returns the updated patient object. |
| **delete_doctor** | username:String | Doctor | Deletes the doctor with the provided username. If successful, returns the deleted doctor object. |
| **read_doctor** | username:String | Doctor | Returns the doctor with the provided username. Returns an error if the doctor does not exist. |
| ----------- | ----------- | ----------- | ----------- |
| **readAll_nurse** | None | [Nurse] | Returns an array of all existing nurses in the system. If no nurse exists, an empty array is returned. |
| **create_nurse** | name:String, note:String, email:String, username:String | Nurse | Creates a nurse with the provided parameters. The username has to be unique. If successful, returns the created nurse object. |
| **update_nurse** | name:String, note:String, email:String, username:String, doctor\_id: String, nurse\_id: String | Nurse | Updates the nurse with the provided username according to the provided parameters. If successful, returns the updated nurse object. |
| **delete_nurse** | username:String | Nurse | Deletes the nurse with the provided username. If successful, returns the deleted nurse object. |
| **read_nurse** | username:String | Nurse | Returns the nurse with the provided username. Returns an error if the nurse does not exist. |

## Data Model ##
The following data model is used for the return parameters. Please make sure to use the exact naming described below.

### Patient: ###

- username: string **(unique)**
- name: string
- email: string
- note: string
- doctor_id: string
- nurse_id: string

Describes a patient. The username is derived in the frontend by using the part of the email before the `@` symbol (or the entire email, if no `@` is present).
The `nurse_id` is currently unused and is expected to be **null**.

### Doctor: ###

- username: string **(unique)**
- name: string
- email: string
- note: string
- department: string

Describes a doctor. The username is derived in the frontend by using the part of the email before the `@` symbol (or the entire email, if no `@` is present).
The `department` is **null** when creating a new doctor and is not supplied in the `create_doctor` method.

### Nurse: ###

- username: string **(unique)**
- name: string
- email: string
- note: string

Describes a nurse. The username is derived in the frontend by using the part of the email before the `@` symbol (or the entire email, if no `@` is present).

## Running the Frontend ##
The frontend is provided only as a built web application, without the clear-text source code. You execute the frontend by opening the `build/index.html` file in a browser (we tested Firefox and Chrome, but others should work).

The frontend assumes that your backend is listening on `localhost` port `8888` (Note: `localhost` is identical to `127.0.0.1`).

To learn how to connect the frontend to your backend, we provide a file called `hospital.if` that is compatible with the interface generator. In this way, you can generate both an example frontend and a backend interface that should be compatible with the actual frontend, but gives you more detailed output and debug possibilities. Additionally, we provide a number of example messages below.

## Example Messages ##
A number of example commands sent by the frontend and corresponding successful answers are provided in the file `examples.txt`.