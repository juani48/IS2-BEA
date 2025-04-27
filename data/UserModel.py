from .AppDataBase import db
from sqlalchemy import Column
from sqlalchemy import Integer, String

class UserModel(db.Model):
    __tablename__ = "user_table" # Nombre de la tabla
    dni = db.Column("dni", db.Integer, primaryKey=True)
    email = db.Column("email", db.String(120), unique=True, nullable=False)
    name = db.Column("name", db.String(50), nullable=False)
    lastname = db.Column("lastname", db.String(50), nullable=False)
    employeeNumber = db.Column("employee_number", db.Integer, nullable=True)
    # relationship
    
    def __repr__(self):
        return "<UserModel %r>" % self.nombre

