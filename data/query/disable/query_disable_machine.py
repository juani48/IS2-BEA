from data.config import session
from data.model.MachineModel import MachineModel

def execute(patent):
    local_machine = session.get(MachineModel, patent)
    local_machine.disable = True
    session.commit()