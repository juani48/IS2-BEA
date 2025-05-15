from data.appDataBase import update_user


def usecase_update_user(dni,name,lastname):
    update_user(
        dni,
        name,
        lastname,
    )
    return True



