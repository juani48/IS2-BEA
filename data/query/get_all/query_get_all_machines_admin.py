from data.config import session
from data.model.MachineModel import MachineModel

def execute():
    machine_list = session.query(MachineModel).all()
    if(machine_list == None):
        raise Exception("No hay maquinarias para mostrar.")
    return machine_list

