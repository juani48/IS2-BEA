import mercadopago

# acces_token_test = APP_USR-5208819603646835-052017-0d91fab01a4d5ecf50714f57ed634e49-2447327823
MP_SDK = mercadopago.SDK("APP_USR-5208819603646835-052017-0d91fab01a4d5ecf50714f57ed634e49-2447327823")
__UNIT__ = 1
__CURRENCY__ = "ARS"
__BASE_URL__ = "https://a3eb-181-231-168-220.ngrok-free.app" # ngrok http http://127.0.0.1:5000 -> Se debe reemplazar esta url por lo que salga en la terminal
__SUCCESS_URL__ = f"{__BASE_URL__}/successful_reservation.html"
__FAILURE_URL__ = f"{__BASE_URL__}/failure_reservation.html"
__PENDING_URL__ = ""
__NOTIFICATION_URL__ = ""

def make_preferences(machine_id, machine_model, unit_price):

    preferences_data = {
        "back_urls": { 
            "success": __SUCCESS_URL__, 
            "failure": __FAILURE_URL__,
        },
        "items": [
            { 
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
        },
        "items": [
            { 
                "title": f"COMPRAR RESERVA DE LA MAQUINA: JAUN_XD - ABC1", 
                "quantity": 1, 
                "unit_price": 10,
                "currency_id": __CURRENCY__,
            }
        ],
    }
    preferences_response = MP_SDK.preference().create(preferences_data)
    return preferences_response["response"]
