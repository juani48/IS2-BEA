from data.appDataBase import delete_reservation

def usecase_cancel_reservation(client_id, machine_id, start_day):
    delete_reservation(client_id, start_day, machine_id)