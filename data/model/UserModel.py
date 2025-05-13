from data.config import Base
from sqlalchemy import Column, Integer, Double, DateTime, ForeignKey, Boolean, String

class UserModel(Base):
    __tablename__ = "user_table"

    dni = Column(Integer, primary_key=True)
    password = Column(String(15), nullable=False)

    email = Column(String(120), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    employee_number = Column(Integer, unique=True, nullable=True)
    
    def __repr__(self):
        return "{" + f"""dni:{self.dni}, password:{self.password}, name:{self.name}, email={self.email}, lastname:{self.lastname}, employeeNumber:{self.employee_number}""" + "}"

    def __init__(self, dni, password, email, name, lastname, employee_number):
        self.dni = dni
        self.password = password
        self.email = email
        self.name = name
        self.lastname = lastname
        self.employee_number = employee_number