from data.config import session
from data.query.get import query_get_user, query_get_employee_by_number

def execute(employeeN, dni):
    local_user = query_get_user.execute(dni)
    if not local_user:
        raise ValueError(f"No se encontró un usuario con DNI {dni}")

    if employeeN == 0:
        # Usa el número actual en negativo, se invierte
        local_user.employee_number *= -1
    else:
        # Verifica que no esté repetido
        empleado_existente = query_get_employee_by_number.execute(employeeN)
        if empleado_existente:
            raise ValueError(f"El número de empleado {employeeN} ya está en uso")
        local_user.employee_number = employeeN

    local_user.type = "Empleado"
    session.commit()
