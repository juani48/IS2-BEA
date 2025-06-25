from data.config import session
from data.model.MachineModel import MachineModel

def execute(machine_number, commentary):
    local_machine = session.get(MachineModel, machine_number)
    if(local_machine == None):
        raise Exception("Máquina inexistente.")
    session.add(commentary)
    session.commit()