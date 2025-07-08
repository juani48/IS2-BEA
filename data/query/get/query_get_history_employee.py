from data.config import session
from data.model.ReservationModel import ReservationModel
from data.model.MaintenanceModel import MaintenanceModel
from data.model.RentModel import RentModel
from data.query.get import query_get_employee_by_number

def execute(empN):
    local_employee = query_get_employee_by_number.execute(empN)
    if (local_employee.employee_number < 0):
        local_employee_id = -local_employee.employee_number 
    else:
        local_employee_id = local_employee.employee_number

    rent_list = session.query(RentModel).filter(RentModel.employee_id == local_employee_id).all()
    reservation_list = session.query(ReservationModel).filter(ReservationModel.employee_id == local_employee_id).all()
    maintenance_start_list = session.query(MaintenanceModel).filter(MaintenanceModel.start_employee_id == local_employee_id).all()
    maintenance_end_list = session.query(MaintenanceModel).filter(MaintenanceModel.end_employee_id == local_employee_id).all()

    result = {
        "rents": [r.json() for r in rent_list] or None,
        "reservations": [r.json() for r in reservation_list] or None,
        "maintenance_started": [m.json() for m in maintenance_start_list] or None,
        "maintenance_ended": [m.json() for m in maintenance_end_list] or None,
    }

    # Si todos son None, devolver None
    if all(value is None for value in result.values()):
        return None

    return result

