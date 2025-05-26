from core.service.mercado_pago import PayByMercadoPago
from data.appDataBase import delete_reservation, update_confirm_reservation
from datetime import datetime

def usecase_confirm_reservation(topic, request):
    merchant_order = None
    if(topic == "payment"):
        id = request.get("resource")
        payment = PayByMercadoPago.get_payment(id)
        merchant_order = PayByMercadoPago.get_merchant_order(payment.get("response").get("order").get("id"))
    elif(topic == "merchant_order"):
        string = request.get("resource")
        list = string.split("/")
        merchant_order = PayByMercadoPago.get_merchant_order(list[-1])
    
    
    total_value = 0
    payments = merchant_order.get("response").get("payments")
    for x in payments:
        if x.get("status") == "approved":
            total_value += x.get("transaction_amount")
    
    reservation_id = merchant_order.get("response").get("items")[-1].get("id")
    reservation_id = reservation_id.split(",")
    machine = reservation_id[1]
    client = reservation_id[0]
    start_day = reservation_id[2]

    if (total_value >= merchant_order.get("response").get("total_amount")):
        # ENVIAR CORREO DE TODO OK
        update_confirm_reservation(client_id=client, start_day=start_day, machine_id=machine)

    else:
        # ENVIAR CORREO QUE NO SE EJECUTO EL PAGO
        
        delete_reservation(client_id=client, start_day=start_day, machine_id=machine)
    

