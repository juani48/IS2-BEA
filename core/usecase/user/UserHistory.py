from core.usecase.reserve import UserReservations
from data.appDataBase import get_all_rents_by_dni

def usecase_user_history(dni):
    reservations = UserReservations.usecase_user_reservations(dni)
    # lista de alquileres
    rents = get_all_rents_by_dni(dni)
    # mergear las dos listas

    return reservations + rents