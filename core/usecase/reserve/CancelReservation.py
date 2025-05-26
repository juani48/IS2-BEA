from data.appDataBase import delete_reservation

def usecase_cancel_reservation(client_id, machine_id, start_day):
    delete_reservation(client_id, start_day, machine_id)

def usecase_cancel_reservation(preferences_id):
    delete_reservation(preference_id=preferences_id)