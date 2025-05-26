from data.model.ReservationModel import ReservationModel
from data.appDataBase import insert_reserve, get_machine
from core.service.mercado_pago import PayByMercadoPago
from datetime import date, datetime

def usecase_add_reserve(start_day, end_day, client_id, machine_id, shipment):
    
    machine = get_machine(machine_id)

    end = datetime.strptime(end_day, "%Y-%m-%d")
    start = datetime.strptime(start_day, "%Y-%m-%d")

    days = (end - start).days
    total_value = machine.price_day * days

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