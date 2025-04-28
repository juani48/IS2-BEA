import os

from config import Base, engine, session
from UserModel import UserModel
from MachineModel import MachineModel
from ReservationModel import ReservationModel
from exception import ExistingRecord
import datetime


def create_database():
    if (not os.path.isfile("///db/database.db")):
        Base.metadata.create_all(engine)


# inserts
def insert_user(user):
    local_user = session.query(UserModel).get(user.dni)
    if (local_user == None):
        session.add(user)
        session.commit()
    else:
        raise ExistingRecord.ExistingRecordException()

def insert_machine(machine):
    local_machine = session.query(MachineModel).get(machine.patent)
    if(local_machine == None):
        session.add(machine)
        session.commit()
    else:
        raise ExistingRecord.ExistingRecordException()
    
def insert_reservation(reservation):
    local_reservation = session.get(ReservationModel, (reservation.start_day, reservation.client_id, reservation.machine_id))
    if(local_reservation == None):
        session.add(reservation)
        session.commit()
    else:
        raise ExistingRecord.ExistingRecordException()

# get all
def get_all_user():
    return session.query(UserModel).all()

def get_all_machine():
    return session.query(MachineModel).all()

def get_all_reservation():
    return session.query(ReservationModel).all()


if __name__ == "__main__":
    create_database()

    #insert_user(UserModel(dni=1, email="email1", name="name1", lastname="lastname1", employee_number=0))
    #insert_user(UserModel(dni=2, email="email2", name="name2", lastname="lastname2", employee_number=1))

    #insert_machine(MachineModel(patent=1, mark="mark1", model="model1", price_day=1.0, ubication="ubication1"))

    #insert_reservation(
        #ReservationModel(
            #start_day=datetime.datetime.now(), 
            #client_id=1, 
            #machine_id=1, 
            #end_day=datetime.datetime.now(), 
            #total_value=1.0,
            #shipment=False
            #)
        #)
    
    print(get_all_user())
    print(get_all_machine())
    print(get_all_reservation())