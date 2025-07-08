from datetime import datetime, timedelta
from data.appDataBase import insert_maintenance, get_machine, update_machine, get_all_rent_by_date, get_all_reservation_by_date, update_cancel_rent
from data.model.MaintenanceModel import MaintenanceModel

def usercase_start_maintenance(start_day, client_id, start_employee_id, machine_id):
    start = datetime.now()
    #start = datetime.strptime(start_day, "%Y-%m-%d.%H-%M-%S")
    end = start + timedelta(days=14)
    start_day = start.strftime("%Y-%m-%d.%H-%M-%S")
    end_day = end.strftime("%Y-%m-%d.%H-%M-%S")
    
    # Poner en mantenimiento la maquina
    machine = get_machine(machine_id)
    machine.under_maintenance = True
    update_machine(patent=machine_id, machine=machine)

    client = 0
    now = datetime.now()

    list_rent = get_all_rent_by_date(None, None)
    #list_reservation = []

    if list_rent:
        list_rent = [x for x in list_rent if x.machine_id == machine_id]

    if list_rent:
        # Buscar el alquiler más cercano a ahora
        closest_rent = min(list_rent, key=lambda x: abs(parse_date(x.start_day) - now))
        client = closest_rent.client_id
        update_cancel_rent(start_day=closest_rent.start_day, client_id=closest_rent.client_id, machine_id=closest_rent.machine_id)
    else:
        list_reservation = get_all_reservation_by_date(None, None)
        if list_reservation:
            list_reservation = [x for x in list_reservation if x.machine_id == machine_id]

        if list_reservation:
            # Buscar la reserva más cercana a ahora
            closest_reservation = min(list_reservation, key=lambda x: abs(parse_date(x.start_day) - now))
            client = closest_reservation.client_id


    maintenance = MaintenanceModel(
        start_day=start_day,
        client_id=client,
        machine_id=machine_id,
        start_employee_id=start_employee_id,
        end_day=end_day
    )

    insert_maintenance(start_day, client_id, start_employee_id, machine_id, maintenance)



def parse_date(date_str):
    # Intenta con formato de alquiler
    try:
        return datetime.strptime(date_str, "%Y-%m-%d.%H-%M-%S")
    except ValueError:
        # Intenta con formato de reserva
        return datetime.strptime(date_str, "%Y-%m-%d")