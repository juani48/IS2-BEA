from sqlalchemy.exc import SQLAlchemyError
from data.config import session
from data.model.UserModel import UserModel

def execute(email):
    if not email:
        raise ValueError("El email no puede ser vacío o None.")

    try:
        user = session.query(UserModel).filter_by(email=email).first()
        return user
    except SQLAlchemyError as e:
        # Podés loguear el error aquí si usás logging
        raise None