from data.config import Base
from sqlalchemy import Column, Integer, Double, DateTime, ForeignKey, Boolean

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