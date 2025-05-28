# usecases/auth.py
from flask_login import logout_user
from data.appDataBase import get_user
from core.entity import User
import bcrypt

def usecase_login(dni, password):
    user_model = get_user(dni)

    if user_model is None:
        raise Exception("Inicio de sesión fallido por credenciales incorrectas.")
    if (user_model.type == "Admin") or (user_model.authorized == 1):         
            if (password == user_model.password): 
                return user_model
    else:
        raise Exception("Inicio de sesión fallido por credenciales incorrectas.")
    
def usecase_logout():
    logout_user()
