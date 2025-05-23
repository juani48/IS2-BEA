from data.config import session
from data.model.UserModel import UserModel


def execute (dni):
    local_user = session.query(UserModel).filter(UserModel.dni == dni).first()
    #if local_user == None:
        #raise Exception("Ya existe la cuenta.")
    #else:
        #local_user = session.get(UserModel,email)

    return local_user