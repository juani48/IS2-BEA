from data.config import session
from data.model.MachineModel import MachineModel
from data.model.ReservationModel import ReservationModel

def execute(patent):
    local_machine = session.get(MachineModel, patent)
    local_machine.disable = True
    session.query(ReservationModel).filter(ReservationModel.machine_id == patent).delete()
    session.commit()