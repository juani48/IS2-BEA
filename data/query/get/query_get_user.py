from data.config import session
from data.model.UserModel import UserModel


def execute (dni):
    local_user = session.get(UserModel,dni)
    return local_user