from data.config import session
from data.model.ReservationModel import ReservationModel
from data.model.MaintenanceModel import MaintenanceModel
from data.model.RentModel import RentModel
from data.query.get import query_get_machine

def execute(machine_patent):
    local_machine = query_get_machine.execute(machine_patent)
    if local_machine is None:
        return None

    rent_list = session.query(RentModel).filter(RentModel.machine_id == local_machine.patent
    ).all()
    reservation_list = session.query(ReservationModel).filter(ReservationModel.machine_id == local_machine.patent
    ).all()
    maintenance_list = session.query(MaintenanceModel).filter(MaintenanceModel.machine_id == local_machine.patent
    ).all()

    result = {
        "rents": [r.json() for r in rent_list] or None,
        "reservations": [r.json() for r in reservation_list] or None,
        "maintenances": [m.json() for m in maintenance_list] or None,
    }

    # Si todos son None, devolver None
    if all(value is None for value in result.values()):
        return None

    return result

