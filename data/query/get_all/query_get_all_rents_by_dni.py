from data.config import session
from data.model.RentModel import RentModel

def execute(client_id):
    return session.query(RentModel).filter(RentModel.client_id == client_id).all()
    