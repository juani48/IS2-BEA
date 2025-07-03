from data.config import session
from data.model.UserModel import UserModel

def execute(employeeN):
    local_employee = session.query(UserModel).filter(UserModel.employee_number == employeeN).first()
    return local_employee
