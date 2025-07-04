from data.appDataBase import get_machine, update_end_maintenance, update_machine
from data.model.MaintenanceModel import MaintenanceModel
from datetime import datetime

def usercase_end_maintenance(start_day, client_id, start_employee_id, machine_id, end_employee_id, description):

    # LOCALDATE.NOW() END_DAY

    machine = get_machine(machine_id)
    machine.under_maintenance = True
    update_machine(machine_id,machine)

    end = datetime.now()
    end_day = end.strftime("%Y-%m-%d.%H-%M-%S")

    update_end_maintenance(start_day, client_id, start_employee_id, machine_id, end_employee_id, description, end_day)