from data.model.UserModel import UserModel
from data.appDataBase import insert_employee


def usecase_add_employee(dni, email, name, lastname,phone,dateBirth, employeeN):
    _validator(dni, email, name, lastname)
    user = UserModel(
            dni=int(dni),
            email= email,
            name= name,
            lastname= lastname,
            phone = phone,
            dateBirth = dateBirth,
            employeeN= employeeN
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
    
    