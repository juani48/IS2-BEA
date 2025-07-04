from data.appDataBase import get_user

def usecase_get_user_by_dni(dni):
    try:
        return get_user(dni)
    except Exception:
        return None
