from data.appDataBase import get_all_reservations
from datetime import datetime

def usecase_get_daily_reservations():
    list = get_all_reservations()
    local_date = datetime.now()
    new_list = []
    for x in list:
        date = x.start_day
        str_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        if(local_date >= str_date):
            new_list.append(x)
    return new_list