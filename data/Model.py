from config import Base
from sqlalchemy import Column, Integer, Double, DateTime, ForeignKey, Boolean, String

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

# ------------------------------------------------------------------------- #

class ReservationModel(Base):
   __tablename__ = "reservation_table"

   #id = Column(Integer, primary_key=True)
   #composite_id = Column(composite(start_day, client_id, machine_id), unique=True) # Atributo compuesto
   start_day = Column(DateTime, nullable=False, primary_key=True)
   client_id = Column(Integer, ForeignKey("user_table.dni"), nullable=False, primary_key=True)
   machine_id = Column(Integer, ForeignKey("machine_table.patent"), nullable=False, primary_key=True)
   

   end_day = Column(DateTime, nullable=False)
   total_value = Column(Double, nullable=False)
   shipment = Column(Boolean, nullable=False) # Envio

   def __repr__(self):
      return "{" + f"""start_day:{self.start_day}, client_id:{self.client_id}, machine_id:{self.machine_id}, end_day:{self.end_day}, total_value:{self.total_value}, shipment:{self.shipment}""" + "}"

   def __init__(self, start_day, client_id, machine_id, end_day, total_value, shipment):
      self.start_day = start_day
      self.client_id = client_id
      self.machine_id = machine_id
      self.end_day = end_day
      self.total_value = total_value
      self.shipment = shipment

# ------------------------------------------------------------------------- #

class MachineModel(Base):
    __tablename__ = "machine_table"

    patent = Column(Integer, primary_key=True)
    mark = Column(String, nullable=False)
    model = Column(String, nullable=False)
    price_day = Column(Double, nullable=False)
    ubication = Column(String, nullable=False)
    # category = Column() # CF de categoria o rubro
    # refund_strategy = Column() # CF de la estrategia de reembolso

    def __repr__(self):
        return "{" + f"""patent:{self.patent}, mark:{self.mark}, model:{self.model}, price_day:{self.price_day}, ubication:{self.ubication}""" + "}"

    def __init__(self, patent, mark, model, price_day, ubication):
        self.patent = patent
        self.mark = mark
        self.model = model
        self.price_day = price_day
        self.ubication = ubication