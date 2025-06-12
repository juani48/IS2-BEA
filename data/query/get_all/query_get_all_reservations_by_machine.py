from sqlalchemy import and_
from data.config import session
from data.model.ReservationModel import ReservationModel
from data.model.RentModel import RentModel

def execute(machine_id):
    return session.query(
        ReservationModel
    ).join(
        RentModel
    ).filter(
        and_(
            ReservationModel.machine_id == machine_id,
            RentModel.machine_id == machine_id
        ) 
    ).all()