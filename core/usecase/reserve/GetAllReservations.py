# usecase_get_all_reservations.py
from data.appDataBase import get_all_reservations

def usecase_get_all_reservations():
    lista = get_all_reservations()
    return [reserva.json() for reserva in lista]
