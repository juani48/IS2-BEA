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
        self.id = str(user_model.dni)  # requerido por Flask-Login

        #Campo necesario para acceder a /session/employee ,soy lara, agregue todo esto hasta abajo para usarlo
        self.employee_number = user_model.employee_number #Lo necesito para el confirmar reserva, no lo saquen

        # Otros campos opcionales si los necesitás en la sesión
        self.phone = user_model.phone
        self.birth_date = user_model.birth_date
        self.points = user_model.points
        self.authorized = user_model.authorized
     