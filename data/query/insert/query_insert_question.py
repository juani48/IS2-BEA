from data.config import session

def execute( question):
    session.add(question)
    session.commit()