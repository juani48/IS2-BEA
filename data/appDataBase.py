import os
from data.config import Base, engine
from data.query.disable import query_disable_categorie, query_disable_machine
from data.query.enable import query_enable_categorie, query_enable_machine
from data.query.get_all import query_get_all_machines, query_get_all_machines_by_categorie
from data.query.insert import query_insert_user, query_insert_machine, query_insert_categorie, query_insert_mc
from data.query.update import query_update_machine

def create_database():
    if (not os.path.isfile("///db/database.db")):
        Base.metadata.create_all(engine)


# ---- inserts -----
def insert_user(dni, user):
    query_insert_user.execute(dni, user)

def insert_machine(patent, categorie, machine, machine_categorie):
    query_insert_machine.execute(patent, machine)
    query_insert_mc.execute(patent, categorie, machine_categorie)
    
def insert_categorie(name, categorie):
    query_insert_categorie.execute(name, categorie)

# ---- disable ----
def disable_categorie(categorie):
    query_disable_categorie.execute(categorie=categorie)

def disable_machine(patent):
    query_disable_machine.execute(patent=patent)

# ---- enable ----
def enable_categorie(categorie):
    query_enable_categorie.execute(categorie=categorie)

def enable_machine(patent):
    query_enable_machine.execute(patent=patent)

# ---- update ----
def update_machine(patent, machine):
    query_update_machine.execute(patent=patent, new_machine=machine)

# ---- get all ----
def get_all_machines():
    return query_get_all_machines.execute()

def get_all_machines_by_categorie(categorie):
    return query_get_all_machines_by_categorie.execute(categorie)