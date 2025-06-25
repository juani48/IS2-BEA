from data.config import session
from data.model.QuestionModel import QuestionModel

def execute():
    return session.query(QuestionModel).all()
