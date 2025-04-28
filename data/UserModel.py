from config import Base
from sqlalchemy import Column, Integer, String

class UserModel(Base):
    __tablename__ = "user_table" # Nombre de la tabla

    dni = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    employeeNumber = Column(Integer, unique=True, nullable=True)
    
    # relationship
    
    def __repr__(self): # Metodo para consultas
        return f"<UserModel(dni={self.dni}, name={self.name}, email={self.email})"

    def __init__(self, dni, email, name):
      self.dni = dni; self.email = email; self.name = name

