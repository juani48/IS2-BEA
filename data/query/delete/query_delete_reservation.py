from sqlalchemy import and_
from data.config import session
from data.model.ReservationModel import ReservationModel

def execute(client_id, start_day, machine_id):
    session.query(
        ReservationModel
    ).filter(
        and_(
            ReservationModel.client_id == client_id,
            ReservationModel.machine_id == machine_id,
            ReservationModel.start_day == start_day
        )
    ).delete()
    session.commit()

def execute(preference_id):
    session.query(
        ReservationModel
    ).filter(
        ReservationModel.preference_id == preference_id
    ).delete()
    session.commit()