from data.appDataBase import update_reservation_to_rent

def usercase_activate_reservation(start_day, client_id, machine_id, employee_id):
    update_reservation_to_rent(start_day, client_id, machine_id, employee_id)