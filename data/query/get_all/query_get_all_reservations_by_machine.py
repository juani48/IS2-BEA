from sqlalchemy import and_
from data.config import session
from data.model.MachineModel import MachineModel
from data.model.ReservationModel import ReservationModel

def execute(machine_id):
    return session.query(
        ReservationModel
    ).filter(
        and_(
            ReservationModel.machine_id == machine_id,
            ReservationModel.paid == True,
        )
    ).all()