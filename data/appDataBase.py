import os
from data.config import Base, engine

from data.query.disable import query_disable_categorie, query_disable_machine,query_disable_employee

from data.query.delete import query_delete_user

from data.query.enable import query_enable_categorie, query_enable_machine, query_enable_user,query_enable_employee

from data.query.get_all import query_get_all_machines, query_get_all_machines_by_categorie, query_get_all_employees, query_get_all_users, query_get_all_categories, query_get_all_reservations_by_machine,query_get_all_requests,query_get_all_reservation, query_get_all_reservations_by_dni

from data.query.insert import query_insert_user, query_insert_machine, query_insert_categorie, query_insert_mc,query_insert_employee, query_insert_reserve, query_TEST_USER

from data.query.update import query_update_machine, query_update_user, query_update_user_points, query_update_confirm_reservation, query_update_user_dni

from data.query.change import query_change_password_user

from data.query.get import query_get_user, query_get_machine, query_get_discount,query_get_employee,query_get_user_by_email

from data.query.delete import query_delete_reservation

from data.query.init import query_init_discount

def create_database():
    if (not os.path.isfile("///db/database.db")):
        Base.metadata.create_all(engine)
        query_init_discount.execute()


# ---- inserts -----
def TEST_USER(dni, user):
    query_TEST_USER.execute(dni, user)
    #query_insert_user.execute(dni, user)


def insert_user(dni, user, email):
    #query_TEST_USER.execute(dni, user)
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

def disable_employee(nro_employee):
    query_disable_employee.execute(nro_employee=nro_employee)

# ---- delete ----
def delete_user(dni):
    query_delete_user.execute(dni=dni)

# ---- enable ----
def enable_categorie(categorie):
    query_enable_categorie.execute(categorie=categorie)

def enable_machine(patent):
    query_enable_machine.execute(patent=patent)

def enable_user(dni):
    query_enable_user.execute(dni=dni)

def enable_employee(nro_employee):
    query_enable_employee.execute(nro_employee)

# ---- update ----
def update_machine(patent, machine):
    query_update_machine.execute(patent=patent, new_machine=machine)

def update_user_points(dni, number):
    query_update_user_points.execute(dni, number)

def update_user(dni, name, lastname):
    query_update_user.execute(dni=dni, new_name= name,new_lastname= lastname)    

def update_confirm_reservation(client_id, start_day, machine_id):
    query_update_confirm_reservation.execute(client_id, start_day, machine_id)

def update_user_dni(dni, new_dni):
    query_update_user_dni.execute(dni, new_dni)

# ---- change  ----
def change_password(dni,password):
    query_change_password_user.execute(dni,password)


# ----  get  -----
def get_user (dni):
    return query_get_user.execute(dni)

def get_user_by_email(email):
    return query_get_user_by_email.execute(email)

def get_machine(machine_id):
    return query_get_machine.execute(machine_id)

def get_discount(name):
    return query_get_discount(name)

def get_employee(employeeN):
    return query_get_employee(employeeN)

# ---- get all ----
def get_all_users():
    return query_get_all_employees.execute()

def get_all_requests():
    return query_get_all_requests.execute()

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

def get_all_reservations():
    return query_get_all_reservation.execute()

def get_all_reservations_by_dni(client_id):
    return query_get_all_reservations_by_dni.execute(client_id)

# ---- delete ---- #
def delete_reservation(client_id, start_day, machine_id):
    query_delete_reservation.execute(client_id, start_day, machine_id)

def delete_reservation(preference_id):
    query_delete_reservation.execute(preference_id)