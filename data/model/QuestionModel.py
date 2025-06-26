from data.config import Base
from sqlalchemy import Column, Integer, String

class QuestionModel(Base):
    __tablename__ = "question_table"

    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=True)
    dni_user = Column(Integer, nullable=False)
    dni_employee = Column(Integer, nullable=True)

    def __init__(self, dni_user, question):
        self.dni_user = dni_user
        self.question = question
        self.answer = None
        self.dni_employee = None

    def json(self):
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "dni_user": self.dni_user,
            "dni_employee": self.dni_employee,
        }
