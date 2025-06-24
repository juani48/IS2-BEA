from data.config import Base
from sqlalchemy import Column, Integer, Double, DateTime, ForeignKey, Boolean, String

class RentModel(Base):
    __tablename__ = "rent_table"

    start_day = Column(String, nullable=False, primary_key=True)
    client_id = Column(Integer, ForeignKey("user_table.dni"), nullable=False, primary_key=True)
    machine_id = Column(String, ForeignKey("machine_table.patent"), nullable=False, primary_key=True)
   
    end_day = Column(String, nullable=False)
    total_value = Column(Double, nullable=False)
    employee_id = Column(String, nullable=True) # Guarda el id empleado que activo

    extended = Column(Boolean, nullable=True, default=False)
    #days_extended = Column(Integer, nullable=True)
    #extended_value = Column(Double, nullable=True)

    def __repr__(self):
        return "{" + f"""start_day:{self.start_day}, client_id:{self.client_id}, machine_id:{self.machine_id}, end_day:{self.end_day}, total_value:{self.total_value}, employee_id:{self.employee_id}, extended: {self.extended}""" + "}" #  days_extended: {self.days_extended}, extended_value: {self.extended_value}

    def json(self):
      return {
            "start_day": self.start_day,
            "client_id": self.client_id,
            "machine_id": self.machine_id,
            "end_day": self.end_day,
            "total_value": self.total_value,
            "employee_id": self.employee_id,
            "extended": self.extended,
            #"days_extended": self.days_extended,
            #"extended_value": self.extended_value
        }
   
    def json_days(self):
      return {
            "start_day": self.start_day,
            "end_day": self.end_day,
        }

    def __init__(self, start_day, client_id, machine_id, end_day, total_value, employee_id):
        self.start_day = start_day
        self.client_id = client_id
        self.machine_id = machine_id
        self.end_day = end_day
        self.total_value = total_value
        self.employee_id = employee_id
        self.extended = False
        #self.days_extended = 0
        #self.extended_value = 0.0
