import json

def usecase_login(dni, password, db):
    if dni == "":
        raise Exception()
    if password == "":
        raise Exception()
    user = db.get_user(dni)
    user = json.loads(user)
    if password != user.get("password"):
        raise Exception()
