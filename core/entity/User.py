# entity/User.py
from flask_login import UserMixin

class User(UserMixin):

  def __init__(self, user_model):
    print("Iniciando User con", user_model)
    self.dni = user_model.dni
    self.name = user_model.name
    self.lastname = user_model.lastname
    self.email = user_model.email
    self.password = user_model.password
    self.type = user_model.type
    self.id = str(user_model.dni)
