import os
from data.config import Base, engine

from data.query.disable import query_disable_categorie, query_disable_machine

from data.query.enable import query_enable_categorie, query_enable_machine

from data.query.get_all import query_get_all_machines, query_get_all_machines_by_categorie, query_get_all_employees, query_get_all_users, query_get_all_categories, query_get_all_reservations_by_machine

from data.query.insert import query_insert_user, query_insert_machine, query_insert_categorie, query_insert_mc,query_insert_employee, query_insert_reserve

from data.query.update import query_update_machine, query_update_user

from data.query.change import query_change_password_user

from data.query.get import query_get_user, query_get_machine

def create_database():
    if (not os.path.isfile("///db/database.db")):
        Base.metadata.create_all(engine)


# ---- inserts -----
def insert_user(dni, user, email):
    query_insert_user.execute(dni, user, email)

def insert_machine(patent, categorie, machine, machine_categorie):
    query_insert_machine.execute(patent, machine)
    query_insert_mc.execute(patent, categorie, machine_categorie)
    
def insert_categorie(name, categorie):
    query_insert_categorie.execute(name, categorie)

def insert_employee(dni, user):
    query_insert_employee.execute(dni,user)

def insert_reserve(start_day, client_id, machine_id, reserve):
    query_insert_reserve.execute(start_day, client_id, machine_id, reserve)

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

def update_user(dni, name, lastname):
    query_update_user.execute(dni=dni, new_name= name,new_lastname= lastname)    

# ---- change  ----
def change_password(dni,password):
    query_change_password_user.execute(dni,password)


# ----   get  -----
def get_user (dni):
    return query_get_user.execute(dni)

def get_machine(machine_id):
    return query_get_machine.execute(machine_id)

# ---- get all ----
def get_all_users():
    return query_get_all_employees.execute()

def get_all_employees():
    return query_get_all_employees.execute()

def get_all_machines():
    return query_get_all_machines.execute()

def get_all_machines_by_categorie(categorie):
    return query_get_all_machines_by_categorie.execute(categorie)

def get_all_categories():
    return query_get_all_categories.execute()

def get_all_reservations_by_machine(machine_id):
    return query_get_all_reservations_by_machine.execute(machine_id)