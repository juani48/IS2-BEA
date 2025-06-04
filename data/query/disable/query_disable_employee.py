from data.config import session
from data.query.get import query_get_user

def execute(dni):
    local_employee = query_get_user.execute(dni)
    local_employee.type = "Cliente"
    local_employee.employee_number = local_employee.employee_number  * -1
    session.commit()