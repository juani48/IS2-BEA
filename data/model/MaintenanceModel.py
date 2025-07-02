from data.config import Base
from sqlalchemy import Column, Integer, Double, DateTime, ForeignKey, Boolean, String

class MaintenanceModel(Base):
    __tablename__ = "maintenance_table"

    start_day = Column(String, nullable=False, primary_key=True)
    client_id = Column(Integer, ForeignKey("user_table.dni"), nullable=False, primary_key=True) # Almaceno el ultimo usuario que uso la maquina
    start_employee_id = Column(Integer, ForeignKey("user_table.employee_number"), nullable=False, primary_key=True)
    machine_id = Column(String, ForeignKey("machine_table.patent"), nullable=False, primary_key=True)
   
    end_day = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    description = Column(String, default="")
    end_employee_id = Column(Integer, ForeignKey("user_table.employee_number"), nullable=True, default=0)


    def __repr__(self):
        return "{" + f"""start_day:{self.start_day}, client_id:{self.client_id}, machine_id:{self.machine_id}, end_day:{self.end_day}, start_employee_id:{self.start_employee_id}, completed: {self.completed}, description: {self.description}, end_employee_id: {self.end_employee_id}""" + "}"

    def json(self):
      return {
            "start_day": self.start_day,
            "client_id": self.client_id,
            "machine_id": self.machine_id,
            "end_day": self.end_day,
            "start_employee_id": self.start_employee_id,
            "completed": self.completed,
            "description": self.description,
            "end_employee_id": self.end_employee_id
        }
   
    def json_days(self):
      return {
            "start_day": self.start_day,
            "end_day": self.end_day,
        }

    def __init__(self, start_day, client_id, machine_id, end_day, start_employee_id):
        self.start_day = start_day
        self.client_id = client_id
        self.machine_id = machine_id
        self.end_day = end_day
        self.start_employee_id = start_employee_id
        self.completed = False
        self.description = ""
        self.end_employee_id = 0