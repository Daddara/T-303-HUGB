# SC-T-303-HUGB - Software Engineering, Fall 2021

* **Group 1**
* This project is developed using specified processes and systematic software engineering practices.

## About the project
The aim of this project is to create a backend for a hospital management system and to be used by hospital staff. 

## Installing
Clone the gitlab repository https://gitlab.com/hugb_21_g_1/hugb-21-g-1.git to an empty folder on your computer. 

Here is how: https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository


## Running the project

* Websockets must be installed `pip install websockets`

* Open two terminals while in program's directory:

* Run the client in one terminal window: 
`python src/HospitalSystem_client.py`

* Run the server in another terminal window: 
`python src/HospitalSystem_ctrl.py`

## Running the frontend

The frontend is provided only as a built web application, without the clear-text source code. You execute the frontend by opening the `build/index.html` file in a browser (Tested on Firefox, Chrome and Safari).

The frontend assumes that your backend is listening on `localhost` port `8888` (Note: `localhost` is identical to `127.0.0.1`).

## Testing

* First you must install coverage and unittest with the following commands:
    `pip install coverage`
    `pip install unittes`

* To test you must run the following command:
    
    `coverage run -m unittest *test.py*`

    where the ** is the name of the test folder.

    and to see the coverage you must run: `coverage report`
    which will show the test coverage

## Dependencies

* `Python`
* `Pip`
* `websockets`
* `coverage`
* `unittest`

* Install requirements (Should be prompted by IDE, if not install manually with `$ pip install -r requirements.txt`)



# Group Members
| GitLab Username          | Student name                  |
| ------------------------ | ----------------------------- |
| @daddara                 | Arnar Már Brynjarsson         |
| @Crazyape                | Daníel Örn Sigurðsson         |
| @hordurh20               | Hörður Snævar Harðarson       |
| @lovisahuld              | Lovísa Huld Friðriksdóttir    |
| @runarorn90              | Rúnar Örn Friðriksson         |
| @tryggvia                | Tryggvi Þór Árnason           |
| @ingunn20                | Ingunn Birta Ómarsdóttir      |

# Code of Conduct

[Code of Conduct](https://gitlab.com/hugb_21_g_1/hugb-21-g-1/-/blob/master/code-of-conduct.md).


#### Reykjavik University
#### T-303-HUGB
