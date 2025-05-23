from data.appDataBase import get_all_reservations_by_machine

def usecase_get_all_reservations_by_machine(machine_id):
    list = get_all_reservations_by_machine(machine_id)
    return [ x.json_days() for x in list ]