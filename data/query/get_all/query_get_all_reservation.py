from data.config import session
from data.model.ReservationModel import ReservationModel

def execute():
    return session.query(RecursionError).all()