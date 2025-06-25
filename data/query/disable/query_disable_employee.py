from data.config import session
from data.query.get import query_get_user

def execute(dni):
    local_employee = query_get_user.execute(dni)
    if not local_employee:
        raise ValueError(f"No se encontró un empleado con DNI {dni}")

    # ✅ Si está habilitado, lo deshabilito
    if local_employee.employee_number > 0:
        local_employee.employee_number *= -1        
        local_employee.type = "Cliente"         # ✅ Cambiar tipo a Cliente (pierde acceso al panel)

    session.commit()
