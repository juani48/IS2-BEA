from sqlalchemy import and_
from data.config import session
from data.model.ReservationModel import ReservationModel


def execute(start_day, client_id, machine_id, reserve):
    local_reservation = session.query(ReservationModel).filter(
        and_(ReservationModel.start_day == start_day,
             ReservationModel.client_id == client_id,
             ReservationModel.machine_id == machine_id)
    ).first()
    if(local_reservation != None):
        raise Exception("Ya existes una reserva.")
    session.add(reserve)
    session.commit()