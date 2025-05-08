import json
from core.exception import NullData

def usecase_login(dni, password, db):
    if dni == "":
        raise NullData.NullDataException()
    if password == "":
        raise NullData.NullDataException()
    user = db.get_user(dni)
    user = json.loads(user)
    if password != user.get("password"):
        raise Exception()
