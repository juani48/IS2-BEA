from data.config import session
from data.model.UserModel import UserModel

def execute():
    user_list = session.query(UserModel).all()
    
    return user_list
