import mercadopago

# Configura tu access token (sandbox o producción)
# acces_token_test = APP_USR-5208819603646835-052017-0d91fab01a4d5ecf50714f57ed634e49-2447327823
MP_SDK = mercadopago.SDK("TU_ACCESS_TOKEN")
__UNIT__ = 1
__CURRENCY__ = "ARS"
__SUCCESS_URL__ = ""
__FAILURE_URL__ = ""
__PENDING_URL__ = ""
__NOTIFICATION_URL__ = ""

#preference_data = {
    #"items": [
        #{
            #"title": "Producto XYZ",
            #"quantity": 1,
            #"unit_price": 100.0,  # Precio en la moneda local
            #"currency_id": "ARS", 
        #}
    #],
    #"back_urls": {
        #"success": "https://tu-app.com/pago-exitoso", # yo usaria "https://bobelalquilador.com/pay/successful_payment"
        #"failure": "https://tu-app.com/pago-fallido",
        #"pending": "https://tu-app.com/pago-pendiente",
    #},
    #"notification_url": "url",  
#}

# Crear la preferencia
#preference_response = sdk.preference().create(preference_data)
#preference = preference_response["response"]

def make_preferences(start_day, end_day, client_id, machine_id, shipment, unit_price):

    title = { 
        "start_day": start_day, 
        "client_id": client_id, 
        "machine_id": machine_id, 
        "end_day": end_day, 
        "shipment": shipment, 
    }

    preferences_data = {
        "items": [{ "title": title, "quatity": __UNIT__, "unit_price": unit_price, "currency_id": __CURRENCY__ }],
        "back_urls": { "succes": __SUCCESS_URL__, "failure": __FAILURE_URL__, "pending": __PENDING_URL__ },
        "notification_url": __NOTIFICATION_URL__ 
    }
    preferences_response = MP_SDK.preference().create(preferences_data)
    return preferences_response["response"]