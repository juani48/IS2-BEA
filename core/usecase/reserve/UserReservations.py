from data.appDataBase import get_all_reservations_by_dni

def usecase_user_reservations(dni):
    list = get_all_reservations_by_dni(dni)
    if list == None:
        raise Exception("No hay reservas o alquileres para mostrar.")
    return list