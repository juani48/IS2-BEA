from sqlalchemy import and_
from data.config import session
from data.model.MachineModel import MachineModel
from data.model.ReservationModel import ReservationModel

def execute(machine_id):
    return session.query(
        ReservationModel
    ).filter(
        ReservationModel.machine_id == machine_id
        #and_(
        #    
            #ReservationModel.paid == True,
        #)
    ).all()