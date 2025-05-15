from operator import and_
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
        and_(
            MachineCategorieModel.categorie_id == categorie,
            MachineModel.disable == False
        ) 
    ).all()

    if(not machine_list):
        raise Exception("No hay maquinas para mostrar de esta categoria")
    return machine_list
