from data.config import session
from data.model.ReservationModel import ReservationModel

def execute():
    reservation_list = session.query(ReservationModel).all()
    if(reservation_list == None):
        raise Exception("No hay reservas para mostrar.")
    return reservation_list
    