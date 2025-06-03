from core.usecase.reserve import UserReservations

def usecase_user_history(dni):
    reservations = UserReservations.usecase_user_reservations(dni)
    # lista de alquileres
    # mergear las dos listas
    return reservations