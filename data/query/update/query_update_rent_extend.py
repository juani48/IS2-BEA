from datetime import datetime
from sqlalchemy import and_
from data.config import session
from data.model.RentModel import RentModel

def exeute(start_day, client_id, machine_id, days_extended, extended_value):
    local_rent = session.query(
        RentModel
    ).filter(
        and_(
            RentModel.client_id == client_id,
            RentModel.machine_id == machine_id,
            RentModel.start_day == start_day
        )
    ).first()

    if( local_rent == None):
        raise Exception("La renta que se quiere extender no existe.")
    
    local_rent.extended = True
    local_rent.days_extended = days_extended
    local_rent.extended_value = extended_value

    session.commit()
    
