from data.appDataBase import get_user


def usecase_get_user_by_dni(dni):
    return get_user(dni)