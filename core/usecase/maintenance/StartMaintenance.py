from datetime import datetime, timedelta
from data.appDataBase import insert_maintenance, get_user, get_machine
from data.model.MaintenanceModel import MaintenanceModel

def usercase_start_maintenance(start_day, client_id, start_employee_id, machine_id):
    start = datetime.strptime(start_day, "%Y-%m-%d")
    end = start + timedelta(days=14)
    end_day = datetime.strftime(end, "%Y-%m-%d")
    
    # Poner en mantenimiento la maquina (?

    maintenance = MaintenanceModel(
        start_day=start_day,
        client_id=client_id,
        machine_id=machine_id,
        start_employee_id=start_employee_id,
        end_day=end_day
    )

    insert_maintenance(start_day, client_id, start_employee_id, machine_id, maintenance)