from data.model.UserModel import UserModel

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
        raise Exception()
    if password == "":
        raise Exception()
    if email == "":
        raise Exception()
    if name == "":
        raise Exception()
    if lastname == "":
        raise Exception()