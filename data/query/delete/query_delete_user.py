from data.config import session
from data.query.get import query_get_user


def execute (dni):
    localUser= query_get_user.execute(dni)
    if (localUser is not None):
        session.delete(localUser)        
        print(f"Usuario con DNI {dni} eliminado correctamente.")
    else:
        print(f"No se encontró un usuario con DNI {dni}.")

    session.commit()