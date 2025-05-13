from data.config import session
from data.model.MachineModel import MachineModel

def execute(patent, machine):
    local_machine = session.query(MachineModel).filter(MachineModel.patent == patent).first()
    if (local_machine != None):
        raise Exception("Maquina existente")
    session.add(machine)
    session.commit()
