from data.model.ReservationModel import ReservationModel
from data.appDataBase import insert_reserve, get_machine, get_discount, update_user_points, update_confirm_reservation
from core.service.mercado_pago import PayByMercadoPago
from datetime import datetime

def usecase_add_reserve(start_day, end_day, client_id, machine_id, shipment, type, apply_discount):
    
    machine = get_machine(machine_id)

    end = datetime.strptime(end_day, "%Y-%m-%d")
    start = datetime.strptime(start_day, "%Y-%m-%d")

    days = (end - start).days
    total_value = machine.price_day * days

    point = int(days/7)
    update_user_points(client_id, point)

    if (type == "Empleado"):
        total_value -= total_value * (0.01 *(get_discount("Employee").discount))
    elif(type == "Client" and apply_discount):
        point = -5
        update_user_points(client_id, point)
        total_value -= total_value * (0.01 * (get_discount("Points").discount))

    preference = PayByMercadoPago.execute(client_id, machine_id, start_day, machine.model, total_value)

    reserve = ReservationModel(
        start_day=start_day, 
        client_id=client_id, 
        machine_id=machine_id, 
        end_day=end_day, 
        total_value=total_value, 
        shipment=shipment,
        preference_id=preference["id"]
    )

    insert_reserve(start, client_id, machine_id, reserve)

    return preference

from data.query.insert import query_insert_reserve

def init_usecase_add_reserve(start_day, end_day, client_id, machine_id, shipment, type, apply_discount):
    
    machine = get_machine(machine_id)

    end = datetime.strptime(end_day, "%Y-%m-%d")
    start = datetime.strptime(start_day, "%Y-%m-%d")

    days = (end - start).days
    total_value = machine.price_day * days

    if (type == "Empleado"):
        total_value -= total_value * (0.01 *(get_discount("Employee").discount))
    elif(type == "Client" and apply_discount):
        point = int(days/7) - 5
        update_user_points(client_id, point)
        total_value -= total_value * (0.01 * (get_discount("Points").discount))

    reserve = ReservationModel(
        start_day=start_day, 
        client_id=client_id, 
        machine_id=machine_id, 
        end_day=end_day, 
        total_value=total_value, 
        shipment=shipment,
        preference_id=f"{start_day}-{client_id}-{machine_id}"
    )
    insert_reserve(start, client_id, machine_id, reserve)
    update_confirm_reservation(client_id,start_day,machine_id)
