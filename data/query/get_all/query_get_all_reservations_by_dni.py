from operator import and_
from data.config import session
from data.model.ReservationModel import ReservationModel

def execute(client_id):
    return session.query(ReservationModel).filter(
        and_(
            ReservationModel.client_id == client_id,
            ReservationModel.activate == False
        )
        ).all()
    