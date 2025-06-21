from datetime import datetime
from data.appDataBase import insert_rent, get_user, get_machine
from data.model.RentModel import RentModel

def usercase_add_rent(start_day, client_id, machine_id, end_day, employee_id):
    end = datetime.strptime(end_day, "%Y-%m-%d")
    start = datetime.strptime(start_day, "%Y-%m-%d")

    days = (end - start).days
    if (days < 7 ):
        raise Exception("Se debe alquilar una maquina con un minimo de 7 dias.")
    
    client = get_user(client_id)
    points = int(days/7)
    client.points += points

    machine = get_machine(machine_id)
    total_value = machine.price_day * days

    rent = RentModel(
        start_day=start_day,
        client_id=client_id,
        machine_id=machine_id,
        total_value=total_value,
        employee_id=employee_id,
        end_day=end_day
    )

    insert_rent(start_day, client_id, machine_id, rent)