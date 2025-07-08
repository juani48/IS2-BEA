from datetime import datetime
from operator import and_
from data.config import session
from data.model.RentModel import RentModel

def execute():
    local_reservation = session.query(
        RentModel
    ).all()

    return local_reservation