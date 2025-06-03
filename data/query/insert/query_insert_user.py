from data.config import session
from data.model.UserModel import UserModel

def execute(dni, user,email):
    # Verificar si ya existe un usuario con el mismo DNI
    local_user = session.get(UserModel, dni)
    if (local_user != None):
        raise Exception("Ya existe un usuario con ese DNI")
    # Verificar si ya existe un usuario con el mismo email
    else:
        if session.query(UserModel).filter(UserModel.email == email).first() is not None:
            raise Exception("Usuario con ese email ya existe")

    # Insertar nuevo usuario
    session.add(user)
    session.commit()
    return True
