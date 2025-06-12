from datetime import datetime
from sqlalchemy import and_
from data.config import session
from data.model.UserModel import UserModel
from data.model.ReservationModel import ReservationModel

def execute(client_id, start_day, machine_id):
    
    local_reservation = session.query(
        ReservationModel
    ).filter(
        and_(
            ReservationModel.client_id == client_id,
            ReservationModel.machine_id == machine_id,
            ReservationModel.start_day == start_day
        )
    ).first()

    __delete_points__(local_reservation)

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

def execute_by_client(preference_id):

    local_reservation = session.query(
        ReservationModel
    ).filter(
        ReservationModel.preference_id == preference_id
    ).first()

    __delete_points__(local_reservation)

    session.query(
        ReservationModel
    ).filter(
        ReservationModel.preference_id == preference_id
    ).delete()
    
    session.commit()


def __delete_points__(local_reservation):

    end_day = local_reservation.end_day
    start_day = local_reservation.start_day

    end = datetime.strptime(end_day, "%Y-%m-%d")
    start = datetime.strptime(start_day, "%Y-%m-%d")

    days = (end - start).days
    points = int(days/7)

    local_client = session.get(UserModel, local_reservation.client_id)
    local_client.points -= points