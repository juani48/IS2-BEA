import hashlib
import mercadopago

__ACCESS_TOKEN_TEST__ = "APP_USR-5208819603646835-052017-0d91fab01a4d5ecf50714f57ed634e49-2447327823"
MP_SDK = mercadopago.SDK(__ACCESS_TOKEN_TEST__)
__UNIT__ = 1
__CURRENCY__ = "ARS"
__BASE_URL__ = "https://1458-181-231-168-220.ngrok-free.app" # ngrok http http://127.0.0.1:5000 -> Se debe reemplazar esta url por lo que salga en la terminal
__SUCCESS_URL__ = f"{__BASE_URL__}/successful_reservation.html"
__FAILURE_URL__ = f"{__BASE_URL__}/failure_reservation.html"
__PENDING_URL__ = f"{__BASE_URL__}/failure_reservation.html"
__NOTIFICATION_URL__ = f"{__BASE_URL__}/pay/pay_notification"

def make_preferences(client_id, machine_id, start_day, machine_model, unit_price):

    preferences_data = {
        "back_urls": { 
            "success": __SUCCESS_URL__, 
            "failure": __FAILURE_URL__,
            "pending": __PENDING_URL__,
        },
        "notification_url": __NOTIFICATION_URL__,
        "items": [
            { 
                "id" : f"{client_id}-{machine_id}-{start_day}",
                "title": f"COMPRAR RESERVA DE LA MAQUINA: {machine_model} - {machine_id}", 
                "quantity": 1, 
                "unit_price": unit_price,
                "currency_id": __CURRENCY__,
            }
        ],
    }
    preferences_response = MP_SDK.preference().create(preferences_data)
    return preferences_response["response"]

def make_preferences_test():

    preferences_data = {
        "back_urls": { 
            "success": __SUCCESS_URL__, 
            "failure": __FAILURE_URL__,
            "pending": __PENDING_URL__,
        },
        "notification_url": __NOTIFICATION_URL__,
        "items": [
            { 
                "id": "ID TANTO",
                "title": f"COMPRAR RESERVA DE LA MAQUINA: JAUN_XD - ABC1", 
                "quantity": 1, 
                "unit_price": 10,
                "currency_id": __CURRENCY__,
            }
        ],
    }
    preferences_response = MP_SDK.preference().create(preferences_data)
    return preferences_response["response"]

def config_get_payment(id):
    return MP_SDK.payment().get(id)

def config_get_merchant_order(id):
    return MP_SDK.merchant_order().get(id)
