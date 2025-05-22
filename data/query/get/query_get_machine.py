from data.config import session
from data.model.MachineModel import MachineModel

def execute(machine_id):
    return session.get(MachineModel, machine_id)