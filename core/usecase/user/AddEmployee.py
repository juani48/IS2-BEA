from data.model.UserModel import UserModel
from data.appDataBase import insert_employee
from core.usecase.user.RequestUser import _random_password

def usecase_add_employee(dni, email, name, lastname, phone, dateBirth, employeeN):
    #_validator(dni, email, name, lastname)

    password = _random_password()
    user = UserModel(
            dni=int(dni),
            password= password,
            email= email,
            name= name,
            lastname= lastname,
            phone = phone,
            birth_date = dateBirth,
            employee_number= employeeN,
            type = "Empleado",
            authorized = True
        )
    insert_employee(
        dni,
        user,
    )
    return True

def _validator(dni, password, email, name, lastname):
    if dni == "":
        raise Exception("El DNI no puede estar vacío")
    if email == "":
        raise Exception("El mail  no puede estar vacío")
    if name == "":
        raise Exception("El nombre  no puede estar vacío")
    if lastname == "":
        raise Exception("El apellido  no puede estar vacío")
    
    