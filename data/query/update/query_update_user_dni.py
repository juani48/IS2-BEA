from data.config import session
from data.model.UserModel import UserModel
from data.model.ReservationModel import ReservationModel

def execute(dni, new_dni):
    if session.get(UserModel, new_dni) is not None:
        raise Exception("Ya existe un usuario con este dni")

        raise Exception("Ya existe un usuario con este dni")

    local_user = session.get(UserModel, dni)
    if not local_user:
        raise Exception("No se encontró el usuario original")

    old_dni = local_user.dni
    local_user.dni = new_dni

    reservations = session.query(ReservationModel).filter(ReservationModel.client_id == old_dni).all()

    for x in reservations:
        x.client_id = new_dni
    session.commit()