from data.model.UserModel import UserModel
from data.appDataBase import insert_user


def usecase_signing(dni, password, email, name, lastname,phone):
    user = UserModel(
            dni=int(dni),
            password= password,
            email= email,
            name= name,
            lastname= lastname,
            phone = phone,
            authorized = False
        )
    insert_user(
        dni,
        user
    )
    return True

