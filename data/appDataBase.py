import os

from data.config import Base, engine, session
from data.model import MachineModel, ReservationModel
from data.query.inseret import query_insert_user, query_insert_machine, query_insert_reservation
from data.model.UserModel import UserModel

def create_database():
    if (not os.path.isfile("///db/database.db")):
        Base.metadata.create_all(engine)


# inserts
def insert_user(dni, user):
    query_insert_user.execute(dni, user)

def insert_machine(patent, machine):
    query_insert_machine.execute(patent, machine)
    
