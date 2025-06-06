from data.config import session
from data.model.UserModel import UserModel

def execute(employeeN):
    return session.query(UserModel).filter(UserModel.employee_number == employeeN).first()
