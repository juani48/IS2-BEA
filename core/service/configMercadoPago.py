import mercadopago

# Configura tu access token (sandbox o producción)
sdk = mercadopago.SDK("TU_ACCESS_TOKEN")

preference_data = {
    "items": [
        {
            "title": "Producto XYZ",
            "quantity": 1,
            "unit_price": 100.0,  # Precio en la moneda local
            "currency_id": "ARS", 
        }
    ],
    "back_urls": {
        "success": "https://tu-app.com/pago-exitoso", # yo usaria "https://bobelalquilador.com/pay/successful_payment"
        "failure": "https://tu-app.com/pago-fallido",
        "pending": "https://tu-app.com/pago-pendiente",
    },
    "auto_return": "approved",  # Redirige automáticamente al éxito si el pago es aprobado
}

# Crear la preferencia
preference_response = sdk.preference().create(preference_data)
preference = preference_response["response"]