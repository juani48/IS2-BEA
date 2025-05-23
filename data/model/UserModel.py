from data.config import Base
from sqlalchemy import Column, Integer, Double, DateTime, ForeignKey, Boolean, String, Date

from data.config import Base  # Asegúrate de que Base esté importado correctamente

class UserModel(Base):
    __tablename__ = "user_table"

    dni = Column(Integer, primary_key=True)
    password = Column(String(15), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    employee_number = Column(Integer, nullable=True, default=0)
    authorized = Column(Boolean, nullable=False, default=False)
    birth_date = Column(String, nullable=False)  # <-- Campo nuevo
    phone = Column(Integer, nullable=False)
    points = Column(Integer, default=0)

    def __repr__(self):
        return "{" + f"""dni:{self.dni}, password:{self.password}, email: {self.email}, name:{self.name}, lastname: {self.lastname}, employee_number: {self.employee_number} , authorized: {self.authorized}, birth_date: {self.birth_date}, phone: {self.phone}, points: {self.points}""" + "}"

    def __init__(self, dni, email, name, lastname, phone, birth_date, password):
        self.dni = dni
        self.email = email
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.birth_date = birth_date
        self.password = password
        self.employee_number = 0
        self.authorized = False
        self.points = 0

