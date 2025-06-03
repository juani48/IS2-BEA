from data.appDataBase import get_all_users

def usecase_get_all_users():
    return [user.json() for user in get_all_users()]
