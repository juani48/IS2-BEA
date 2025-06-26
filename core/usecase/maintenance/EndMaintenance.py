from data.appDataBase import update_end_maintenance
from data.model.MaintenanceModel import MaintenanceModel

def usercase_end_maintenance(start_day, client_id, start_employee_id, machine_id, end_employee_id, description):

    # LOCALDATE.NOW() END_DAY

    update_end_maintenance(start_day, client_id, start_employee_id, machine_id, end_employee_id, description)