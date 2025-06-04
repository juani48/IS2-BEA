from data.config import session
from data.query.get import query_get_user

def execute(employeeN,dni):
    local_employee = query_get_user.execute(dni)
    if not local_employee:
        raise ValueError(f"No se encontró un usuario con DNI {dni}")
    
    local_employee.type = "Empleado"

    if (employeeN == 0):
        local_employee.employee_number = local_employee.employee_number  * -1
    else:
        local_employee.employee_number = employeeN

    session.commit()