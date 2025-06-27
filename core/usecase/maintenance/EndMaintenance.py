from data.appDataBase import get_machine, update_end_maintenance, update_machine
from data.model.MaintenanceModel import MaintenanceModel
import datetime

def usercase_end_maintenance(start_day, client_id, start_employee_id, machine_id, end_employee_id, description):

    # LOCALDATE.NOW() END_DAY

    machine = get_machine(machine_id)
    machine.under_maintenance = True
    update_machine(machine )

    end = datetime.date.now
    end_day = end.strftdime("%Y-%m-%d")

    update_end_maintenance(start_day, client_id, start_employee_id, machine_id, end_employee_id, description, end_day)