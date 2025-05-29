from data.config import session
from data.model.UserModel import UserModel


def execute (user):
    session.add(user)
    session.commit()