from data.config import session
from data.model.UserModel import UserModel

def execute(dni):
    if not dni:
        raise ValueError("DNI no puede ser vacío o nulo")

    try:
        user = session.get(UserModel, dni)
        
        return user
    except Exception as e:
        # Podés loggear el error si querés
        #raise RuntimeError(f"Error al obtener usuario: {e}")
        return None
