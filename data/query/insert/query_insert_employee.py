from data.config import session
from data.query.get import query_get_employee
from data.model.UserModel import UserModel

def execute(employeeN, user):
    local_employee = query_get_employee.execute(employeeN=employeeN)
    if (local_employee != None):
        raise Exception("Empleado existente")
    else:
        session.add(user)
        session.commit()