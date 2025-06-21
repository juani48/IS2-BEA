from data.config import session
from data.model.UserModel import UserModel
from sqlalchemy import or_

def execute(employeeN):
    return session.query(UserModel).filter(
        or_(
            UserModel.employee_number == employeeN,
            UserModel.employee_number == -employeeN
        )
    ).first()
