from data.config import Base
from sqlalchemy import Column, Integer, Double, DateTime, ForeignKey, Boolean, String

class ReservationModel(Base):
   __tablename__ = "reservation_table"

   start_day = Column(DateTime, nullable=False, primary_key=True)
   client_id = Column(Integer, ForeignKey("user_table.dni"), nullable=False, primary_key=True)
   machine_id = Column(Integer, ForeignKey("machine_table.patent"), nullable=False, primary_key=True)
   
   end_day = Column(DateTime, nullable=False)
   total_value = Column(Double, nullable=False)
   shipment = Column(Boolean, nullable=False) # Envio
   activate = Column(Boolean, nullable=False) # Activa
   employee_id = Column(String, nullable=True) # Cuando se activa, se guarda el id empleado que activo
   paid = Column(Boolean, default=False) # Cuando es pagada, es puesto en true

   def __repr__(self):
      return "{" + f"""start_day:{self.start_day}, client_id:{self.client_id}, machine_id:{self.machine_id}, end_day:{self.end_day}, total_value:{self.total_value}, shipment:{self.shipment}, activate:{self.activate}, employee_id:{self.employee_id}, paid: {self.paid}""" + "}"

   def json(self):
      return {
         "start_day": self.start_day.strftime("%d/%m/%Y %H:%M:%S"),
         "client_id": self.client_id,
         "machine_id": self.machine_id,
         "end_day": self.end_day.strftime("%d/%m/%Y %H:%M:%S"),
         "total_value": self.total_value,
         "shipment": self.shipment,
         "activate": self.activate,
         "employee_id": self.employee_id,
         "paid": self.paid
      }
   
   def json_days(self):
      return {
         "start_day": self.start_day.strftime("%d/%m/%Y %H:%M:%S"),
         "end_day": self.end_day.strftime("%d/%m/%Y %H:%M:%S"),
      }

   def __init__(self, start_day, client_id, machine_id, end_day, total_value, shipment):
      self.start_day = start_day
      self.client_id = client_id
      self.machine_id = machine_id
      self.end_day = end_day
      self.total_value = total_value
      self.shipment = shipment
      self.activate = False
      self.employee_id = None
      self.paid = False