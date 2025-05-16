from data.config import session
from data.model.UserModel import UserModel

def execute(dni, new_name,new_lastname):
    local_user = session.get(UserModel, dni)

    local_user.name = new_name
    local_user.lastname = new_lastname

    session.commit()