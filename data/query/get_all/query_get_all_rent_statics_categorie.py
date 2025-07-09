from datetime import datetime
from operator import and_
from data.config import session
from data.model.MachineCategorieModel import MachineCategorieModel
from data.model.RentModel import RentModel

def execute(categorie):
    local_rent = session.query(
        RentModel
    ).join(
        MachineCategorieModel, MachineCategorieModel.machine_id == RentModel.machine_id
    ).filter(
        MachineCategorieModel.categorie_id == categorie
    ).all()

    return local_rent
