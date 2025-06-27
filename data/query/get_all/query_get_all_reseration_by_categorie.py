from datetime import datetime
from operator import and_
from data.config import session
from data.model.ReservationModel import ReservationModel
from data.model.MachineCategorieModel import MachineCategorieModel

def execute(start_date, end_date, categorie):
    local_reservation = session.query(
        ReservationModel
    ).join(
        MachineCategorieModel, MachineCategorieModel.machine_id == ReservationModel.machine_id
    ).filter(
        and_(
            and_(
                and_(
                    start_date <= ReservationModel.start_day,
                    end_date >= ReservationModel.end_day,
                ),
                and_(
                    ReservationModel.activate == False,
                    ReservationModel.paid == True
                )
            ),
            MachineCategorieModel.categorie_id == categorie
        )
    ).all()

    return local_reservation
