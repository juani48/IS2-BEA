from data.config import session
from data.query.get import query_get_user, query_get_employee_by_number

def execute(employeeN, dni):
    local_employee = query_get_user.execute(dni)
    if not local_employee:
        raise ValueError(f"No se encontró un empleado con DNI {dni}")

    if employeeN == 0:
        if (local_employee.employee_number < 0) and (local_employee.type != "Admin"):
            local_employee.employee_number *= -1    # Usa el número actual en negativo, se invierte
            local_employee.type = "Empleado"
    else:
        # Verifica que no esté repetido
        empleado_existente = query_get_employee_by_number.execute(employeeN)
        if empleado_existente:
            raise ValueError(f"El número de empleado {employeeN} ya está en uso")
        local_employee.employee_number = employeeN
        local_employee.type = "Empleado"
    
    session.commit()
