from operator import and_
from data.config import session
from data.model.ReservationModel import ReservationModel

def execute(client_id, start_day, machine_id):
    local_reservation = session.query(
        ReservationModel
    ).filter(
        and_(
            and_(ReservationModel.client_id == client_id, ReservationModel.machine_id == machine_id,),
            ReservationModel.start_day == start_day)
    ).first()

    if (local_reservation != None):
        local_reservation.paid = True
        session.commit()