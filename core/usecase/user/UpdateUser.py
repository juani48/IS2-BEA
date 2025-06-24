from data.appDataBase import update_user

def usecase_update_user(dni, name, lastname, phone):
    update_user(dni, name, lastname, phone)
    return True



