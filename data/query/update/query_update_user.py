from data.config import session
from data.model.UserModel import UserModel

def execute(dni, new_user):
    local_user = session.get(UserModel, dni)

    local_user.name = new_user.name
    local_user.lastname = new_user.lastname

    session.commit()