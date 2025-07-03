from data.config import Base
from sqlalchemy import Column, Integer, String, Text

class CommentaryModel(Base):
    __tablename__ = "commentary_table"

    date = Column (String ,primary_key=True)
    dni = Column(Integer, nullable= False)
    commentary = Column(String, nullable=False)
    machine_patent = Column(String ,nullable=False)
    answer = Column(Text, nullable = True)

    def __init__(self, date,dni, commentary, machine_patent,answer):
        self.date = date
        self.dni = dni
        self.commentary = commentary
        self.machine_patent = machine_patent
        self.answer = answer

    def json(self):
        return {
            "date": self.date,
            "dni": self.dni,
            "commentary": self.commentary,
            "machine_patent": self.machine_patent,
            "answer": self.answer
        }
