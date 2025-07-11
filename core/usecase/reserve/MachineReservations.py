from data.appDataBase import get_all_reservations_by_machine, get_all_rent_by_date

def usecase_get_all_reservations_by_machine(machine_id):
    list = get_all_reservations_by_machine(machine_id) 
    rent = get_all_rent_by_date(None, None)
    rent = [x for x in rent if x.machine_id == machine_id]
    list = list + rent
    print(list)
    return [ x.json_days() for x in list ]


def usecase_get_all_reservations_by_machine_user_hystory(machine_id):
    print("sss")
    list = get_all_reservations_by_machine(machine_id) 
    #rent = get_all_rent_by_date(None, None)
    #rent = [x for x in rent if x.machine_id == machine_id]
    #list = list + rent
    print(list)
    return [ x.json_days() for x in list ]
