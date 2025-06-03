from sqlalchemy import and_
from data.config import session
from data.model.MachineModel import MachineModel
from data.model.MachineCategorieModel import MachineCategorieModel

def execute(categorie):
    machine_list = session.query(
        MachineModel
    ).join(
        MachineCategorieModel,
        MachineCategorieModel.machine_id == MachineModel.patent
    ).filter(
        MachineCategorieModel.categorie_id == categorie
    ).all()

    if(not machine_list):
        raise Exception("No hay maquinarias para mostrar.")
    return machine_list
