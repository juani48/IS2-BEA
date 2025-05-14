import json
from data.config import session


def usecase_login(dni, password, db):
    if dni == "":
        raise Exception("El DNI no puede estar vacío")
    if password == "":
        raise Exception("La contraseña no puede estar vacía")
    
    session.get
    user = db.get_user(dni)
    user = json.loads(user)
    if password != user.get("password"):
        raise Exception()
