from data.config import Base
from sqlalchemy import Column, Integer, Double, DateTime, ForeignKey, Boolean, String

class ReservationInProccesModel(Base):
     __tablename__ = "reservation_in_procces_table"

     start_day = Column(DateTime, nullable=False, primary_key=True)
     client_id = Column(Integer, ForeignKey("user_table.dni"), nullable=False, primary_key=True)
     machine_id = Column(Integer, ForeignKey("machine_table.patent"), nullable=False, primary_key=True)

     def __repr__(self):
          return "{" + f"""start_day:{self.start_day}, client_id:{self.client_id}, machine_id:{self.machine_id}""" + "}"
     
     def json(self):
          return {
               "start_day": self.start_day.strftime("%d/%m/%Y %H:%M:%S"),
               "client_id": self.client_id,
               "machine_id": self.machine_id,
          }
     
     def __init__(self, start_day, client_id, machine_id):
          self.start_day = start_day
          self.client_id = client_id
          self.machine_id = machine_id
