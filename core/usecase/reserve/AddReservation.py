from data.model.ReservationModel import ReservationModel
from data.appDataBase import insert_reserve

# validar usuario, maquina -> deribar compra
def usecase_add_reserve(start_day, end_day, client_id, machine_id, total_value, shipment):

    reserve = ReservationModel(
        start_day=start_day, client_id=client_id, machine_id=machine_id, 
        end_day=end_day, total_value=total_value, shipment=shipment
    )

    insert_reserve(start_day, client_id, machine_id, reserve)