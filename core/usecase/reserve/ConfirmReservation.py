from core.service.mercado_pago import PayByMercadoPago
from data.appDataBase import delete_reservation, update_confirm_reservation
from core.usecase.service.SendMail import usecase_send_mail
from data.appDataBase import get_user

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
    reservation_id = reservation_id.split("&")
    machine = reservation_id[1]
    client = reservation_id[0]
    start_day = reservation_id[2]

    user = get_user(client)

    if (total_value >= merchant_order.get("response").get("total_amount")):
       
        usecase_send_mail(
            emailDest=user.email, 
            subject="Su pago se realizo exitosamente", 
            body=f"""
                Hola {user.name} {user.lastname},

                ¡Su pago se realizo exitosamente y su reserva fue realizada con exito!

                Comprobante:

                    - ID del cliente: {merchant_order.get("response").get("collector").get("id")}
                    - Compra a nombre de: {merchant_order.get("response").get("collector").get("nickname")}
                    - ID de compra: {merchant_order.get("response").get("id")}
                    - Total pagado: {merchant_order.get("response").get("total_amount")}
                    - Fecha de compra: {merchant_order.get("response").get("date_created")}
                    - ID del producto: {merchant_order.get("response").get("items")[-1].get("id")}

                Gracias por confiar en nosotros. Que disfrute su compra.

                Saludos cordiales,  
                Sistema de Gestión BEA.
                """
            )
        update_confirm_reservation(client_id=client, start_day=start_day, machine_id=machine)

    else:
        usecase_send_mail(
            emailDest=user.email, 
            subject="Su pago no fue realizo", 
            body=f"""
                Hola {user.name} {user.lastname},

                ¡Hubo un problema con su pago!

                Contactese con un empleado y le resolvera la incidencia. Su dinera sera reintegrado.

                Gracias por confiar en nosotros, perdone las molestias. 

                Saludos cordiales,  
                Sistema de Gestión BEA.
                """
            )
        delete_reservation(client_id=client, start_day=start_day, machine_id=machine)
    

