from datetime import datetime, timedelta
from data.appDataBase import update_rent_extend, get_rent, get_all_reservations_by_machine, get_machine

def usecase_extend_rent(start_day, client_id, machine_id, end_day):
    local_rent = get_rent(start_day, machine_id, client_id)
    end = datetime.strptime(end_day, "%Y-%m-%d")

    list = get_all_reservations_by_machine(machine_id)
    list = [x.json_days() for x in list]

    for days in list:
        start = datetime.strptime(days.get("start_day"), "%Y-%m-%d") 
        start -= timedelta(days=14)
        if(start <= end):
            raise Exception("No es posible extender el alquiler, no hay un minimo de 2 semanas de diferencia con la proxima reserva.")
    
    start = datetime.strptime(start_day, "%Y-%m-%d") 
    machine = get_machine(machine_id)
    days = (end - start).days
    value = machine.price_day * days + local_rent.total_value

    update_rent_extend(
        start_day=start_day,
        client_id=client_id,
        machine_id=machine_id,
        end_days_extended=end_day,
        extended_value=value
    )