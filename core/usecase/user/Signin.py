from data.model.UserModel import UserModel
from data.appDataBase import insert_user


def usecase_signing(dni, password, email, name, lastname, phone, birthDate):
    user = UserModel(
            #dni=int(dni),
            dni=dni,
            password= password,
            email= email,
            name= name,
            lastname= lastname,
            phone = phone,
            birth_date=birthDate
        )
    insert_user(
        dni,
        user
    )
    return True

