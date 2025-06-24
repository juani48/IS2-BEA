from datetime import datetime, timedelta
from data.appDataBase import update_rent_extend, get_rent, get_all_reservations_by_machine, get_machine

def usecase_extend_rent(start_day, client_id, machine_id, days_extended):
    local_rent = get_rent(start_day, machine_id, client_id)
    end = datetime.strptime(local_rent.end_day, "%Y-%m-%d")
    end = end + timedelta(days=days_extended)

    list = get_all_reservations_by_machine(machine_id)
    list = [x.json_days() for x in list]

    for days in list:
        start = datetime.strptime(days.get("start_day"), "%Y-%m-%d") 
        start -= timedelta(days=14)
        if(start == end):
            raise Exception("No es posible extender el alquiler, no hay un minimo de 2 semanas de diferencia con la proxima reserva.")
    machine = get_machine(machine_id)
    value = machine.price_day * days_extended

    update_rent_extend(
        start_day=start_day,
        client_id=client_id,
        machine_id=machine_id,
        days_extended=days_extended,
        extended_value=value
    )