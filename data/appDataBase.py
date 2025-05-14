import os
from data.config import Base, engine
from data.query.insert import query_insert_user, query_insert_machine, query_insert_categorie, query_insert_mc
from data.query.delete import query_delete_categorie, query_delete_machine
from data.query.update import query_update_machine

def create_database():
    if (not os.path.isfile("///db/database.db")):
        Base.metadata.create_all(engine)


# inserts
def insert_user(dni, user):
    query_insert_user.execute(dni, user)

def insert_machine(patent, categorie, machine, machine_categorie):
    query_insert_machine.execute(patent, machine)
    query_insert_mc.execute(patent, categorie, machine_categorie)
    
def insert_categorie(name, categorie):
    query_insert_categorie.execute(name, categorie)

# deletes
def delete_categorie(categorie):
    query_delete_categorie.execute(categorie=categorie)

def delete_machine(patent):
    query_delete_machine.execute(patent=patent)

# update
def update_machine(patent, machine):
    query_update_machine.execute(patent=patent, new_machine=machine)