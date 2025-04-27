# El encargado de las consultas SQL
#from entity import UserModel
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config) # Carga la configuracion de la base de datos
db = SQLAlchemy(app)
    
db.create_all() 
nuevo_usuario = UserModel(1, nombre='Juan Pérez', email='juan@ejemplo.com')
db.session.add(nuevo_usuario)
db.session.commit()
print(UserModel.query.all())

if __name__ == "__main__":
    app.run(debug=True)