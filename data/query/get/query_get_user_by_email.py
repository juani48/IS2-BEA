from data.config import session
from data.model.UserModel import UserModel

def execute(email):
    local_employee = session.query(UserModel).filter(UserModel.email == email).first()
    return local_employee