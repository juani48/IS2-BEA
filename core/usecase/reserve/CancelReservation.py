from data.appDataBase import delete_reservation_by_employee, delete_reservation_by_client

def usecase_cancel_reservation_by_employee(client_id, machine_id, start_day):
    delete_reservation_by_employee(client_id, start_day, machine_id)

def usecase_cancel_reservation_by_client(preference_id):
    delete_reservation_by_client(preference_id=preference_id)
