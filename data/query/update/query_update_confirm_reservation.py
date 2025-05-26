from data.config import session
from data.model.ReservationModel import ReservationModel

def execute(client_id, start_day, machine_id):
    local_reservation = session.get(ReservationModel, (client_id, start_day, machine_id))
    local_reservation.paid = True
    session.commit()