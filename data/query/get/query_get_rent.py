from sqlalchemy import and_
from data.config import session
from data.model.RentModel import RentModel

def execute(start_day, machine_id, clien_id):
    local_rent = session.query(
        RentModel
    ).filter(
        and_(
            RentModel.client_id == clien_id,
            RentModel.machine_id == machine_id,
            RentModel.start_day == start_day
        )
    ).first()

    if(local_rent == None):
        raise Exception("No existe el alquiler.")

    return local_rent