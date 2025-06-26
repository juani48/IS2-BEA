from data.config import Base
from sqlalchemy import Column, Integer, String, Float

class CommentaryModel(Base):
    __tablename__ = "commentary_table"

    id = Column (Integer ,primary_key=True)
    machine_patent = Column(String ,nullable=False)
    commentary = Column(String, nullable=False)
    dni = Column(Integer, nullable= False)

    def __init__(self, dni, commentary, machine_patent):
        self.dni = dni
        self.commentary = commentary
        self.machine_patent = machine_patent

    def json(self):
        return {
            "commentary": self.commentary,
            "dni": self.dni,
            "machine_patent": self.machine_patent
        }
