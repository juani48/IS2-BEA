from data.config import session
from data.model.UserModel import UserModel

def execute(dni, user):
    # Verificar si ya existe un usuario con el mismo DNI
    #if session.query(UserModel).filter(UserModel.dni == dni).first() is not None:
    #    raise Exception("Usuario con ese DNI ya existe")

    # Verificar si ya existe un usuario con el mismo email
    #if session.query(UserModel).filter(UserModel.email == email).first() is not None:
    #    raise Exception("Usuario con ese email ya existe")

    # Insertar nuevo usuario
    session.add(user)
    session.commit()
