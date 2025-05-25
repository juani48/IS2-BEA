from data.config import session
from data.model.UserModel import UserModel

def execute(employeeN, user):
    local_employee = session.query(UserModel).filter(UserModel.employee_number == employeeN).first()
    if (local_employee != None):
        raise Exception("Empleado existente")
    else:
        session.add(user)
        session.commit()