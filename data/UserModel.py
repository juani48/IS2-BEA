from config import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class UserModel(Base):
    __tablename__ = "user_table"

    dni = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    employee_number = Column(Integer, unique=True, nullable=True)
    
    def __repr__(self):
        return "{" + f"""dni:{self.dni}, name:{self.name}, email={self.email}, astname:{self.lastname}, employeeNumber:{self.employee_number}""" + "}"

    def __init__(self, dni, email, name, lastname, employee_number):
        self.dni = dni
        self.email = email
        self.name = name
        self.lastname = lastname
        self.employee_number = employee_number

    #def __init__(self, dni, email, name, lastname):
        #self.dni = dni
        #self.email = email
        #self.name = name
        #self.lastname = lastname
