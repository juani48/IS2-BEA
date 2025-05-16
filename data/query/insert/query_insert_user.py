from data.config import session
from data.model.UserModel import UserModel

def execute(dni, user,email):
    local_user = session.query(UserModel).filter(UserModel.dni == dni).first()
    if (local_user != None):
        raise Exception("Usuario existente")
    
    local_user = session.query(UserModel).filter(UserModel.email == email).first()
    if(local_user != None):
        raise Exception("Mail existente")


    session.add(user)
    session.commit()
