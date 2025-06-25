from data.config import Base
from sqlalchemy import Column, Integer, String

class QuestionModel(Base):
    __tablename__ = "question_table"

    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=True)
    name_user = Column(String(50), nullable=False)
    name_employee = Column(String(50), nullable=True)

    def __init__(self, name_user, question, answer=None, name_employee=None):
        self.name_user = name_user
        self.question = question
        self.answer = answer
        self.name_employee = name_employee

    def json(self):
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "name_user": self.name_user,
            "name_employee": self.name_employee,
        }
