from datetime import datetime
from operator import and_
from data.config import session
from data.model.RentModel import RentModel
from data.model.MachineCategorieModel import MachineCategorieModel

def execute(start_date, end_date, categorie):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    local_reservation = session.query(
        RentModel
    ).join(
        MachineCategorieModel.machine_id == RentModel.machine_id
    ).filter(
        and_(
            and_(
                start <= datetime.strptime(RentModel.start_day, "%Y-%m-%d"),
                end >= datetime.strptime(RentModel.end_day, "%Y-%m-%d"),
            ),
            MachineCategorieModel.categorie_id == categorie
        )
    ).all()

    return local_reservation