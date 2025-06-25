from data.config import Base
from sqlalchemy import Column, Integer, String, Float

class CommentaryModel(Base):
    __tablename__ = "commentary_table"

    machine_number = Column(String ,primary_key=True,nullable=False)
    commentary = Column(String, nullable=False)
    name = Column(String(50), nullable= False)

    def __init__(self, name, commentary, machine_number):
        self.name = name
        self.commentary = commentary
        self.machine_number = machine_number

    def json(self):
        return {
            "commentary": self.commentary,
            "name": self.name,
            "machine_number": self.machine_number
        }
