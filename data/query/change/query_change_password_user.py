from data.config import session
from data.model.UserModel import UserModel

def execute (dni,password):
        local_user = session.get(UserModel, dni)

        local_user.password = password

        session.commit()
