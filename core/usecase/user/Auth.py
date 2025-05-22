# usecases/auth.py
from flask_login import login_user, logout_user
from data.appDataBase import get_user
from core.entity import User
import bcrypt

def usecase_login(dni, password):
    
    user_model = get_user(dni)
    if user_model is None:
        raise Exception("Inicio de sesión fallido por credenciales incorrectas.")

    if bcrypt.checkpw(password.encode('utf-8'), user_model.password.encode('utf-8')):
        user = User(user_model)
        login_user(user)
        return user
    else:
        raise Exception("Inicio de sesión fallido por credenciales incorrectas.")

def usecase_logout():
    logout_user()
