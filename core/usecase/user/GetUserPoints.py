from data.appDataBase import get_user

def usecase_get_user_points(client_id):
    user = get_user(client_id)
    return user.points