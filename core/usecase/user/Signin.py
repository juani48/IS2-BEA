from data.model.UserModel import UserModel
from data.appDataBase import insert_user


def usecase_signing(dni, password, email, name, lastname, employee_number, db):
    _validator(dni, password, email, name, lastname)
    user = UserModel(
            dni=int(dni),
            password= password,
            email= email,
            name= name,
            lastname= lastname,
            employee_number= employee_number
        )
    insert_user(
        dni,
        user,
        email
    )
    return True

def _validator(dni, password, email, name, lastname):
    if dni == "":
        raise Exception("El DNI no puede estar vacío")
    if password == "":
        raise Exception("La contraseña no puede estar vacía")
    if email == "":
        raise Exception("El mail  no puede estar vacío")
    if name == "":
        raise Exception("El nombre  no puede estar vacío")
    if lastname == "":
        raise Exception("El apellido  no puede estar vacío")