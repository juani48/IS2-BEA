from core.service.mercado_pago.config import make_preferences

def execute(request_value):

    # Buscar como se realizar las operaciones de fechas
    days = (request_value.get("start_day") - request_value.get("end_day")).days
    unit_price = days * request_value.get("price_day")

    preference = make_preferences(
        start_day=request_value.get("start_day"),
        end_day=request_value.get("end_day"),
        client_id=request_value.get("client_id"),
        machine_id=request_value.get("machine_id"),
        shipment=request_value.get("shipment"),
        unit_price=unit_price
    )
    return preference["init_point"]  # URL de Mercado Pago

#
# from datetime import datetime

# Definir fechas
#fecha1 = datetime.strptime("2021-12-25", "%Y-%m-%d")
#fecha2 = datetime.strptime("2021-12-31", "%Y-%m-%d")

# Calcular la diferencia
#diferencia = fecha2 - fecha1
#print(f"La diferencia es de {diferencia.days} días")
# 
# 
# 
# 