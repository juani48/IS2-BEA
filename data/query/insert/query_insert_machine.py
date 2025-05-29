from data.config import session
from data.model.MachineModel import MachineModel

def execute(patent, machine):
    local_machine = session.get(MachineModel, patent)
    if (local_machine != None):
        raise Exception("Cargada fallida por patente ya existente.")
    session.add(machine)
    session.commit()
