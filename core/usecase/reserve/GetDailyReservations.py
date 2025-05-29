from data.appDataBase import get_all_reservations
from datetime import datetime

def usecase_get_daily_reservations():
    list = get_all_reservations()
    local_date = datetime.now()
    new_list = []

    for x in list:
        date = x.start_day
        try:
            str_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue

        if local_date >= str_date:
            new_list.append({
                "cliente": x.client_id,
                "maquina": x.machine_id,
                "fecha_inicio": x.start_day,
                "fecha_fin": x.end_day,
                "total": x.total_value
            })

    return new_list
