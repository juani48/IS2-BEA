from data.config import session
from data.model.ReservationModel import ReservationModel

def execute(client_id):
    return session.query(ReservationModel).filter(ReservationModel.client_id == client_id).all()