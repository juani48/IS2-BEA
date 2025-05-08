from data.Model import UserModel
from core.exception import NullData

def usecase_singing(dni, password, email, name, lastname, employee_number, db):
    _validator(dni, password, email, name, lastname)
    user = UserModel(
            dni=int(dni),
            password= password,
            email= email,
            name= name,
            lastname= lastname,
            employee_number= employee_number
        )
    db.insert_user(dni, user)
    return True

def _validator(dni, password, email, name, lastname):
    if dni == "":
        raise NullData.NullDataException()
    if password == "":
        raise NullData.NullDataException()
    if email == "":
        raise NullData.NullDataException()
    if name == "":
        raise NullData.NullDataException()
    if lastname == "":
        raise NullData.NullDataException()