from config import Base
from sqlalchemy import Column, Integer, Double, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import composite

class ReservationModel(Base):
   __tablename__ = "reservation_table"

   start_day = Column(DateTime, nullable=False)
   client_id = Column(Integer, ForeignKey("user_table.dni"), nullable=False)
   machine_id = Column(Integer, ForeignKey("machine_table.patent"), nullable=False)
   id = Column(composite(start_day, client_id, machine_id), unique=True, nullable=False) # Atributo compuesto

   end_day = Column(DateTime, nullable=False)
   total_value = Column(Double, nullable=False)
   shipment = Column(Boolean, nullable=False) # Envio

   def __repr__(self):
      return "{" + f"""start_day:{self.start_day}, 
         client_id:{self.client_id}, 
         machine_id:{self.machine_id}, 
         end_day:{self.end_day}, 
         total_value:{self.total_value}
         shipment:{self.shipment}""" + "}"




