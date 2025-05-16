from data.config import session
from data.model.UserModel import UserModel

def execute():
    employees_list = session.query(UserModel).filter(UserModel.employee_number != None).all()
    
    return employees_list