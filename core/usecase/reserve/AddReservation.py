from data.model.ReservationModel import ReservationModel
from data.appDataBase import insert_reserve, get_machine
from core.service.mercado_pago import PayByMercadoPago

def usecase_add_reserve(start_day, end_day, client_id, machine_id, shipment):
    machine = get_machine(machine_id)
    days = (end_day - start_day).days
    total_value = machine.price_day * days
    reserve = ReservationModel(start_day=start_day, client_id=client_id, machine_id=machine_id, end_day=end_day, total_value=total_value, shipment=shipment)
    insert_reserve(start_day, client_id, machine_id, reserve)

    return PayByMercadoPago.execute(client_id, machine_id, start_day, machine.model, total_value)