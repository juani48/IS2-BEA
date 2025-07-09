from data.config import session
from data.model.UserModel import UserModel

def execute(dni):
    if not dni:
        raise ValueError("Alquiler fallido por usuario no registrado.")

    try:
        user = session.get(UserModel, dni)
        
        return user
    except Exception as e:
        # Podés loggear el error si querés
        #raise RuntimeError(f"Error al obtener usuario: {e}")
        return None
