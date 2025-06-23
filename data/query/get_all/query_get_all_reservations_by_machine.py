from sqlalchemy import and_
from data.config import session
from data.model.ReservationModel import ReservationModel
from data.model.RentModel import RentModel

def execute(machine_id):
    return session.query(
        ReservationModel
    ).join(
        RentModel,
        and_(
            ReservationModel.start_day == RentModel.start_day,
            ReservationModel.client_id == RentModel.client_id,
            ReservationModel.machine_id == RentModel.machine_id
        )
    ).filter(
        ReservationModel.machine_id == machine_id
    ).all() #esta parte la tuve que cambiar porque estaba tirando errores