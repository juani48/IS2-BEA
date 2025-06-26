from datetime import datetime
from operator import and_
from data.config import session
from data.model.ReservationModel import ReservationModel
from data.model.MachineCategorieModel import MachineCategorieModel

def execute(start_date, end_date, categorie):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    local_reservation = session.query(
        ReservationModel
    ).join(
        MachineCategorieModel.machine_id == ReservationModel.machine_id
    ).filter(
        and_(
            and_(
                and_(
                    start <= datetime.strptime(ReservationModel.start_day, "%Y-%m-%d"),
                    end >= datetime.strptime(ReservationModel.end_day, "%Y-%m-%d"),
                ),
                and_(
                    ReservationModel.activate == False,
                    ReservationModel.paid == True
                )
            ),
            MachineCategorieModel.categorie_id.lower() == categorie.lower()
        )
    ).all()

    return local_reservation