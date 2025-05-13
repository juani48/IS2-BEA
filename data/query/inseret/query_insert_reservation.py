from data.config import session
from data.model.ReservationModel import ReservationModel

def execute(star_day, client_id, machine_id, reservation):
    local_reservation = session.query(ReservationModel).filter(
        ReservationModel.star_day == star_day & 
        ReservationModel.client_id == client_id &
        ReservationModel.machine_id == machine_id).first()
    if (local_reservation != None):
        raise Exception("Reserva existente")
    session.add(reservation)
    session.commit()
