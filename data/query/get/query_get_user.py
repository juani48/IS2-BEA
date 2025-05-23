from data.config import session
from data.model.UserModel import UserModel


def execute (dni):
    
    if (dni != 0):
        local_user = session.get(UserModel,dni)
    #else:
        #local_user = session.get(UserModel,email)

    return local_user