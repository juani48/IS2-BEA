from data.config import session
from data.model.MachineCategorieModel import MachineCategorieModel

def execute(patent):
    session.query(MachineCategorieModel).filter(MachineCategorieModel.machine_id == patent).delete()
    session.commit()