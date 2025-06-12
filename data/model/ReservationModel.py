from data.config import Base
from sqlalchemy import Column, Integer, Double, DateTime, ForeignKey, Boolean, String

class ReservationModel(Base):
   __tablename__ = "reservation_table"

   start_day = Column(String, nullable=False, primary_key=True)
   client_id = Column(Integer, ForeignKey("user_table.dni"), nullable=False, primary_key=True)
   machine_id = Column(Integer, ForeignKey("machine_table.patent"), nullable=False, primary_key=True)
   
   end_day = Column(String, nullable=False)
   total_value = Column(Double, nullable=False)
   shipment = Column(Boolean, nullable=False) # Envio
   activate = Column(Boolean, nullable=False) # Activa, cuando inicia el alquiler, se activa
   employee_id = Column(String, nullable=True) # Cuando se activa, se guarda el id empleado que activo
   paid = Column(Boolean, default=False) # Cuando es pagada, es puesto en true
   preference_id = Column(String,  nullable=True, unique=True)

   def __repr__(self):
      return "{" + f"""start_day:{self.start_day}, client_id:{self.client_id}, machine_id:{self.machine_id}, end_day:{self.end_day}, total_value:{self.total_value}, shipment:{self.shipment}, activate:{self.activate}, employee_id:{self.employee_id}, paid: {self.paid}, preference_id: {self.preference_id}""" + "}"

   def json(self):
      return {
         "start_day": self.start_day,
         "client_id": self.client_id,
         "machine_id": self.machine_id,
         "end_day": self.end_day,
         "total_value": self.total_value,
         "shipment": self.shipment,
         "activate": self.activate,
         "employee_id": self.employee_id,
         "paid": self.paid,
         "preference_id": self.preference_id
      }
   
   def json_days(self):
      return {
         "start_day": self.start_day,
         "end_day": self.end_day,
      }

   def __init__(self, start_day, client_id, machine_id, end_day, total_value, shipment, preference_id):
      self.start_day = start_day
      self.client_id = client_id
      self.machine_id = machine_id
      self.end_day = end_day
      self.total_value = total_value
      self.shipment = shipment
      self.activate = False
      self.employee_id = None
      self.paid = False
      self.preference_id = preference_id