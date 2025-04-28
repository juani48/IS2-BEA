from config import Base, engine, session, DB_FILE, DB_PATH
from UserModel import UserModel
import os

def create_database():
    if (not os.path.isfile("///db/database.db")):
        Base.metadata.create_all(engine)

def insert_user(user):
    local_user = session.query(UserModel).get(user.dni)
    if (local_user == None):
        session.add(user)
        session.commit()
    else:
        raise RepositoryException()

def get_all_user():
    return session.query(UserModel).all()


if __name__ == "__main__":
    print(session.query(UserModel).all())


class RepositoryException(Exception):
    pass