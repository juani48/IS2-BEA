from core.service.mercado_pago import PayByMercadoPago
from data.appDataBase import delete_reservation_by_employee, update_confirm_reservation
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
                ¡Hola {user.name}!

                ¡RESERVA CONFIRMADA!
                Tu pago se completó con éxito y todo está listo para disfrutar de tu experiencia

                DETALLES DE TU COMPRA:
                ----------------------------------
                Cliente ID: {merchant_order.get("response").get("collector").get("id")}
                Compra a nombre de: {merchant_order.get("response").get("collector").get("nickname")}
                ID de compra: {merchant_order.get("response").get("id")}
                Total pagado: {merchant_order.get("response").get("total_amount")}
                Fecha de compra: {merchant_order.get("response").get("date_created")}
                ID del producto: {merchant_order.get("response").get("items")[-1].get("id")}
                ----------------------------------

                ¡Que disfrutes tu experiencia!
                
                ¿Preguntas o necesitas ayuda con tu reserva? Estamos disponibles para ayudarte en cualquier momento.
                
                Saludos cordiales, El equipo de Bob El Alquilador 
                
                ---
                Este comprobante es válido como respaldo de tu transacción. Recuerda que puedes acceder a tus reservas en cualquier momento desde tu perfil.
                """
            )
        update_confirm_reservation(client_id=client, start_day=start_day, machine_id=machine)

    else:
        usecase_send_mail(
            emailDest=user.email, 
            subject="Su pago no fue realizado", 
            body=f"""
                ¡Hola {user.name}!
                
                ¡UPS! HUBO UN INCONVENIENTE CON TU PAGO
                
                Lamentamos informarte que tu transacción no pudo completarse. Pero no te preocupes:
                
                1. TU DINERO ESTÁ SEGURO y será reintegrado automáticamente en 1-3 días hábiles
                2. Nuestro equipo ya fue notificado y está listo para ayudarte
                
                Por favor contáctanos para resolverlo rápidamente:
                soporte@bobealquilador.com
                
                Horario de atención:
                Lunes a Viernes: 9:00 - 17:00
                
                Sabemos lo frustrante que puede ser y AGRADECEMOS PROFUNDAMENTE TU PACIENCIA. Valoramos tu confianza y haremos todo lo posible para solucionarlo cuanto antes.
                
                Con aprecio,
                El equipo de Bob El Alquilador
                
                ---
                Este mensaje se generó automáticamente. Para respuestas inmediatas, por favor responde directamente este correo.
                """
            )
        delete_reservation_by_employee(client_id=client, start_day=start_day, machine_id=machine)
    

