from data.config import session
from data.model.UserModel import UserModel


def execute (dni):
    local_user = session.get(UserModel,dni)
    if local_user == None:
        raise Exception("El usuario no existe.")
    return local_user