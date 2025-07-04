import os
from data.config import Base, engine

from data.query.disable import query_disable_categorie, query_disable_machine,query_disable_employee

from data.query.delete import query_delete_mc, query_delete_user

from data.query.enable import query_enable_categorie, query_enable_machine, query_enable_user,query_enable_employee

from data.query.get_all import query_get_all_commentarys, query_get_all_machines, query_get_all_machines_by_categorie, query_get_all_employees, query_get_all_users, query_get_all_categories, query_get_all_reservations_by_machine,query_get_all_requests,query_get_all_reservation,query_get_all_reservations_by_dni, query_get_all_reservations_by_dni,query_get_all_disable_employees, query_get_all_machines_admin, query_get_all_machines_by_categorie_admin, query_get_all_maintenance, query_get_all_rent_by_date, query_get_all_reseration_by_date, query_get_all_rent_by_categorie, query_get_all_reseration_by_categorie, query_get_all_rents_by_dni

from data.query.insert import query_insert_user, query_insert_machine, query_insert_categorie, query_insert_mc,query_insert_employee, query_insert_reserve, query_TEST_USER, query_insert_rent, query_insert_maintenance,query_insert_commentary,query_insert_answer

from data.query.update import query_update_machine, query_update_user, query_update_user_points, query_update_confirm_reservation, query_update_user_dni, query_update_reservation_to_rent, query_update_rent_extend, query_update_end_maintenance

from data.query.change import query_change_password_user

from data.query.get import query_get_user, query_get_machine, query_get_discount,query_get_employee,query_get_user_by_email, query_get_rent,query_get_commentary

from data.query.delete import query_delete_reservation

from data.query.init import query_init_discount

def create_database():
    if (not os.path.isfile("///db/database.db")):
        Base.metadata.create_all(engine)
        query_init_discount.execute()

def insertar_tabla():
    Base.metadata.create_all(bind=engine)

# ---- inserts -----
def TEST_USER(dni, user):
    query_TEST_USER.execute(dni, user)
    #query_insert_user.execute(dni, user)


def insert_user(dni, user, email):
    #query_TEST_USER.execute(dni, user)
    query_insert_user.execute(dni, user, email)

def insert_machine(patent, machine):
    query_insert_machine.execute(patent, machine)

def insert_machine_categorie(patent, categorie, machine_categorie):
    query_insert_mc.execute(patent, categorie, machine_categorie)
    
def insert_categorie(name, categorie):
    query_insert_categorie.execute(name, categorie)

def insert_employee(dni, user):
    query_insert_employee.execute(dni,user)

def insert_reserve(start_day, client_id, machine_id, reserve):
    query_insert_reserve.execute(start_day, client_id, machine_id, reserve)

def insert_rent(start_day, client_id, machine_id, rent):
    query_insert_rent.execute(start_day, client_id, machine_id, rent)

def insert_maintenance(start_day, client_id, start_employee_id, machine_id, maintenance):
    query_insert_maintenance.execute(start_day, client_id, start_employee_id, machine_id, maintenance)

    
def insert_commentary(machine_patent,commentary):
    query_insert_commentary.execute(machine_patent, commentary)

def insert_answer(dateID,answerID):
    query_insert_answer.execute(dateID= dateID, answerID= answerID)
    
# ---- disable ----
def disable_categorie(categorie):
    query_disable_categorie.execute(categorie=categorie)

def disable_machine(patent):
    query_disable_machine.execute(patent=patent)

def disable_employee(dni):
    query_disable_employee.execute(dni=dni)

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

def enable_employee(nro_employee,dni):
    query_enable_employee.execute(nro_employee,dni)

# ---- update ----
def update_machine(patent, machine):
    query_update_machine.execute(patent=patent, new_machine=machine)

def update_user_points(dni, number):
    query_update_user_points.execute(dni, number)

def update_user(dni, name, lastname, phone):
    query_update_user.execute(dni=dni, new_name= name,new_lastname= lastname, new_phone = phone)    

def update_confirm_reservation(client_id, start_day, machine_id):
    query_update_confirm_reservation.execute(client_id, start_day, machine_id)

def update_user_dni(dni, new_dni):
    query_update_user_dni.execute(dni, new_dni)

def update_reservation_to_rent(start_day, client_id, machine_id, employee_id):
    query_update_reservation_to_rent.execute(start_day, client_id, machine_id, employee_id)

def update_rent_extend(start_day, client_id, machine_id, end_days_extended, extended_value):
    query_update_rent_extend.exeute(start_day, client_id, machine_id, end_days_extended, extended_value)

def update_end_maintenance(start_day, client_id, start_employee_id, machine_id, end_employee_id, description, end_day):
    query_update_end_maintenance.execute(start_day, client_id, start_employee_id, machine_id, end_employee_id, description, end_day)

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
    return query_get_discount.query_get_discount(name)

def get_employee(employeeN):
    return query_get_employee.execute(employeeN)

def get_rent(start_day, machine_id, clien_id):
    return query_get_rent.execute(start_day, machine_id, clien_id)

def get_commentary (date):
    return query_get_commentary.execute(date)

# ---- get all ----
def get_all_users():
    return query_get_all_users.execute()

def get_all_requests():
    return query_get_all_requests.execute()

def get_all_employees():
    return query_get_all_employees.execute()

def get_all_disable_employees():
    return query_get_all_disable_employees.execute()

def get_all_machines():
    return query_get_all_machines.execute()

def get_all_machines_admin():
    return query_get_all_machines_admin.execute()

def get_all_machines_by_categorie(categorie):
    return query_get_all_machines_by_categorie.execute(categorie)

def get_all_machines_by_categorie_admin(categorie):
    return query_get_all_machines_by_categorie_admin.execute(categorie)

def get_all_categories():
    return query_get_all_categories.execute()

def get_all_reservations_by_machine(machine_id):
    return query_get_all_reservations_by_machine.execute(machine_id)

def get_all_reservations():
    return query_get_all_reservation.execute()

def get_all_reservations_by_dni(client_id):
    return query_get_all_reservations_by_dni.execute(client_id)

def get_all_rents_by_dni(client_id):
    return query_get_all_rents_by_dni.execute(client_id)

def get_all_maintenance():
    return query_get_all_maintenance.execute()

def get_all_reservation_by_date(start_date, end_date):
    return query_get_all_reseration_by_date.execute(start_date, end_date)

def get_all_rent_by_date(start_date, end_date):
    return query_get_all_rent_by_date.execute(start_date, end_date)
    
def get_all_rent_by_categoire(start_date, end_date, categorie):
    return query_get_all_rent_by_categorie.execute(start_date, end_date, categorie)

def get_all_reservation_by_categorie(start_date, end_date, categorie):
    return query_get_all_reseration_by_categorie.execute(start_date, end_date, categorie)

def get_all_questions():
    return #query_get_all_questions.execute()

def get_all_commentarys(machine_patent):
    return query_get_all_commentarys.execute(machine_patent)

# ---- delete ---- #
def delete_reservation_by_employee(client_id, start_day, machine_id):
    query_delete_reservation.execute(client_id, start_day, machine_id)

def delete_reservation_by_client(preference_id):
    query_delete_reservation.execute_by_client(preference_id)

def delete_machine_categorie(patent):
    query_delete_mc.execute(patent)