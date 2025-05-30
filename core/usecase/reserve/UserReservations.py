from data.appDataBase import get_all_reservations_by_dni

def usecase_user_reservations(dni):
    return get_all_reservations_by_dni(dni)