from data.config import session
from data.model.MachineModel import MachineModel

def execute(patent, new_machine):
    local_machine = session.get(MachineModel, patent)
    
    local_machine.mark = new_machine.mark
    local_machine.model = new_machine.model
    local_machine.price_day = new_machine.price_day
    local_machine.refund = new_machine.refund
    local_machine.ubication = new_machine.ubication
    local_machine.refund = new_machine.refund
    local_machine.disable = new_machine.disable
    local_machine.description = new_machine.description
    local_machine.under_maintenance = new_machine.under_maintenance

    session.commit()