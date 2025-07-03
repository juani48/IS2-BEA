from datetime import datetime, timedelta
from data.appDataBase import insert_maintenance, get_machine, update_machine, get_all_rent_by_date, get_all_reservation_by_date
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

    list_rent = get_all_rent_by_date(None, None)
    if list_rent != []:
        list_rent = [x for x in list_rent if x.machine_id == machine_id]
        rent = sorted(list_rent, key=lambda x: x.start_day)[0]
        if (datetime.now() >= datetime.strptime(rent.start_day, "%Y-%m-%d.%H-%M-%S")) and (datetime.now() <= datetime.strptime(rent.end_day, "%Y-%m-%d.%H-%M-%S")):
            client = rent.client_id
    else:
        list_reservation = get_all_reservation_by_date(None, None)
        if list_reservation != []:
            list_reservation = [x for x in list_reservation if x.machine_id == machine_id]
            reservation = sorted(list_reservation, key=lambda x: x.start_day)[0]
            if (datetime.now() >= datetime.strptime(reservation.start_day, "%Y-%m-%d")) and (datetime.now() <= datetime.strptime(reservation.end_day, "%Y-%m-%d")):
                client = reservation.client_id


    maintenance = MaintenanceModel(
        start_day=start_day,
        client_id=client,
        machine_id=machine_id,
        start_employee_id=start_employee_id,
        end_day=end_day
    )

    insert_maintenance(start_day, client_id, start_employee_id, machine_id, maintenance)