from data.appDataBase import get_all_reservations
from datetime import datetime

def usecase_get_daily_reservations():
    list = get_all_reservations()
    local_date = datetime.now()
    new_list = []

    for x in list:
        str_date = x.start_day
        date = datetime.strptime(str_date, "%Y-%m-%d")

        if local_date >= date:
            new_list.append(
                {
                "cliente": x.client_id,
                "maquina": x.machine_id,
                "fecha_inicio": x.start_day,
                "fecha_fin": x.end_day,
                "total": x.total_value
                }
            )

    if(new_list.count() == 0):
        raise Exception("No hay reservas que inician hoy o antes.")

    return new_list
