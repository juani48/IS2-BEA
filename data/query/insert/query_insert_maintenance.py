from sqlalchemy import and_
from data.config import session
from data.model.MaintenanceModel import MaintenanceModel

def execute(start_day, client_id, start_employee_id, machine_id, maintenance):
<<<<<<< HEAD
    local_maintenance = (
    session.query(MaintenanceModel)
    .filter(
=======
    local_maintenance = session.query(
        MaintenanceModel
    ).filter(
>>>>>>> 94125584ee4fcf2145d4b3959cfc5c9699d6041f
        and_(
            MaintenanceModel.start_day == start_day,
            MaintenanceModel.client_id == client_id,
            MaintenanceModel.start_employee_id == start_employee_id,
            MaintenanceModel.machine_id == machine_id
        )
    )
    .first()
)

    if(local_maintenance != None):
        raise Exception("La maquina ya se encuentra en mantenimiento.")
    session.add(maintenance)
    session.commit()