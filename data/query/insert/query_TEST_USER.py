from data.config import session
from data.model.UserModel import UserModel


def execute (dni, user):
    local_user = session.get(UserModel, dni)
    if (local_user != None):
        raise Exception("AAAAAAAAA bbbb")
    session.add(user)
    session.commit()