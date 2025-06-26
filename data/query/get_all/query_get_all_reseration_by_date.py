from datetime import datetime
from operator import and_
from data.config import session
from data.model.ReservationModel import ReservationModel

def execute(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    local_reservation = session.query(
        ReservationModel
    ).filter(
        and_(
            and_(
                start <= datetime.strptime(ReservationModel.start_day, "%Y-%m-%d"),
                end >= datetime.strptime(ReservationModel.end_day, "%Y-%m-%d"),
            ),
            and_(
                ReservationModel.activate == False,
                ReservationModel.paid == True
            )
        )
    ).all()

    return local_reservation