from sqlalchemy import and_
from data.config import session
from data.model.RentModel import RentModel

def execute(start_day, client_id, machine_id, rent):
    local_rent = session.query(RentModel).filter(
        and_(RentModel.start_day == start_day,
             RentModel.client_id == client_id,
             RentModel.machine_id == machine_id)
    ).first()
    if(local_rent != None):
        raise Exception("La maquina tiene un alquiler activo.")
    session.add(rent)
    session.commit()