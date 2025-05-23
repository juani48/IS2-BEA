from data.config import session
from data.model.UserModel import UserModel

def execute(dni, number):
    local_user = session.get(UserModel, dni)
    if (local_user == None):
        raise Exception("El usurio no existe.")
    local_user.points += number
    session.commit()