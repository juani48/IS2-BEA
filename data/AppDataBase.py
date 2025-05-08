import os

from data.config import Base, engine, session
from data.Model import UserModel, MachineModel, ReservationModel
from data.exception import ExistingRecord, NonExistingRecord
#import datetime


def create_database():
    if (not os.path.isfile("///db/database.db")):
        Base.metadata.create_all(engine)


# inserts
def insert_user(dni, user):
    local_user = session.query(UserModel).filter(UserModel.dni == dni).first()
    if (local_user != None):
        raise Exception("Usuario existente")
    session.add(user)
    session.commit()
    

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

# get by primary key
def gel_user(dni):
    local_user = session.query(UserModel).get(dni)
    if local_user == None:
        raise NonExistingRecord.NonExistingRecordException()
    return local_user

#if __name__ == "__main__":
    #create_database()

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
    
    #print(get_all_user())
    #print(get_all_machine())
    #print(get_all_reservation())