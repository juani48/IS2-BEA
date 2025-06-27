from datetime import datetime
from operator import and_
from data.config import session
from data.model.RentModel import RentModel
from data.model.MachineCategorieModel import MachineCategorieModel

def execute(start_date, end_date, categorie):
    local_reservation = session.query(
        RentModel
    ).join(
        MachineCategorieModel, MachineCategorieModel.machine_id == RentModel.machine_id
    ).filter(
        MachineCategorieModel.categorie_id == categorie
    ).all()

    return local_reservation

        #and_(
            #and_(
                #start_date <= RentModel.start_day,
                #end_date >= RentModel.end_day,
            #),
            #MachineCategorieModel.categorie_id == categorie
        #)