from sqlalchemy import and_
from data.config import session
from data.model.MaintenanceModel import MaintenanceModel

def execute(start_day, client_id, start_employee_id, machine_id, maintenance):
    local_maintenance = session.query(
        MaintenanceModel
    ).filter(
        and_(
            and_(
                MaintenanceModel.start_day == start_day,
                MaintenanceModel.client_id == client_id
            ),
            and_(
                MaintenanceModel.start_employee_id == start_employee_id,
                MaintenanceModel.machine_id == machine_id
            )
        )
    ).first()
    if(local_maintenance != None):
        raise Exception("La maquina ya se encuentra en mantenimiento.")
    session.add(maintenance)
    session.commit()