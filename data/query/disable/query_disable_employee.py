from data.config import session
from data.query.get import query_get_employee

def execute(employeeN):
    local_employee = query_get_employee.execute(employeeN=employeeN)
    local_employee.authorized = 0
    session.commit()