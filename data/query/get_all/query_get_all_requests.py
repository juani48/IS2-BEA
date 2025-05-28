from data.config import session
from data.model.UserModel import UserModel

def execute():
    requests_list = session.query(UserModel).filter(UserModel.authorized == 0,UserModel.type == "Cliente").all()
    if(requests_list == None):
        raise Exception("No hay solicitudes que mostrar")
    return requests_list
