from operator import and_
from data.config import session
from data.model.RentModel import RentModel

def execute(client_id):
    return session.query(RentModel).filter(
        and_(
            RentModel.client_id == client_id,
            RentModel.canceled_by_maintenance == False
        )).all()
    