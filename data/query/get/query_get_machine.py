from data.config import session
from data.model.MachineModel import MachineModel

def execute(machine_id):
    local_machine = session.get(MachineModel, machine_id)
    if local_machine == None:
        raise Exception("La maquina no existe.")
    return local_machine