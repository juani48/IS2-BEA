from data.config import session
from data.model.MachineCategorieModel import MachineCategorieModel

def execute(patent, categorie, machine_categorie):
    local_mc = session.query(MachineCategorieModel).filter(
        MachineCategorieModel.machine_id == patent &
        MachineCategorieModel.categorie_id == categorie
        ).first()
    if (local_mc != None):
        raise Exception("La maquina ya tiene esta categoria")
    session.add(machine_categorie)
    session.commit()