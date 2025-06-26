from sqlalchemy import and_
from data.config import session
from data.model.MaintenanceModel import MaintenanceModel

def execute(start_day, client_id, start_employee_id, machine_id, end_employee_id, description):
    local_maintenance = session.query(
        MaintenanceModel
    ).filter(
        and_(
            and_(
                and_(
                    MaintenanceModel.start_day == start_day,
                    MaintenanceModel.client_id == client_id
                ),
                and_(
                    MaintenanceModel.start_employee_id == start_employee_id,
                    MaintenanceModel.machine_id == machine_id
                )
            ),
            MaintenanceModel.completed == False
        )
    ).first()
    if(local_maintenance == None):
        raise Exception("La maquina no tiene un mantenimiento activo.")
    
    local_maintenance.completed = True
    #local_maintenance.end_day = date
    local_maintenance.end_employee_id = end_employee_id
    local_maintenance.description = description
    session.commit()