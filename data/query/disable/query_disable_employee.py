from data.config import session
from data.query.get import query_get_user

def execute(dni):
    local_employee = query_get_user.execute(dni)

    # ✅ Cambiar tipo a Cliente (pierde acceso al panel)
    local_employee.type = "Cliente"

    # ✅ Si está habilitado, lo deshabilito
    if local_employee.employee_number > 0:
        local_employee.employee_number *= -1

    session.commit()
