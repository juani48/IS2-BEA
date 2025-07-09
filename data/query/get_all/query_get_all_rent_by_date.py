from datetime import datetime
from operator import and_
from data.config import session
from data.model.RentModel import RentModel

def execute(start_date, end_date):
    #start = datetime.strptime(start_date, "%Y-%m-%d")
    #end = datetime.strptime(end_date, "%Y-%m-%d")
    local_reservation = session.query(
        RentModel
    ).filter(RentModel.canceled_by_maintenance == False).all()
    print(local_reservation)
    return local_reservation



#and_(
           # start <= datetime.strptime(RentModel.start_day, "%Y-%m-%d"),
        #    end >= datetime.strptime(RentModel.end_day, "%Y-%m-%d"),
        #)