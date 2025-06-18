from data.config import Base
from sqlalchemy import Column, Integer, Double, DateTime, ForeignKey, Boolean, String

class MaintenanceModel(Base):
    __tablename__ = "maintenance_table"

    start_day = Column(String, nullable=False, primary_key=True)
    client_id = Column(Integer, ForeignKey("user_table.dni"), nullable=False, primary_key=True) # Almaceno el ultimo usuario que uso la maquina
    employee_id = Column(Integer, ForeignKey("user_table.employee_number"), nullable=False, primary_key=True)
    machine_id = Column(Integer, ForeignKey("machine_table.patent"), nullable=False, primary_key=True)
   
    end_day = Column(String, nullable=False)
    completed = Column(Boolean, default=False)


    def __repr__(self):
        return "{" + f"""start_day:{self.start_day}, client_id:{self.client_id}, machine_id:{self.machine_id}, end_day:{self.end_day}, employee_id:{self.employee_id}, completed: {self.completed}""" + "}"

    def json(self):
      return {
            "start_day": self.start_day,
            "client_id": self.client_id,
            "machine_id": self.machine_id,
            "end_day": self.end_day,
            "employee_id": self.employee_id,
            "completed": self.completed
        }
   
    def json_days(self):
      return {
            "start_day": self.start_day,
            "end_day": self.end_day,
        }

    def __init__(self, start_day, client_id, machine_id, end_day, employee_id):
        self.start_day = start_day
        self.client_id = client_id
        self.machine_id = machine_id
        self.end_day = end_day
        self.employee_id = employee_id
        self.completed = False