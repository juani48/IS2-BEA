from data.model.UserModel import UserModel
from data.appDataBase import insert_user


def usecase_signing(dni, password, email, name, lastname, phone, birthDate):
    user = UserModel(
             dni=int(dni),
    password=password,
    email=email,
    name=name,
    lastname=lastname,
    phone=int(phone),
    birth_date=birthDate,
    employee_number=0,
    type="Cliente",
    authorized=True
        )
    insert_user(
        dni,
        user, email
    )
    return True

