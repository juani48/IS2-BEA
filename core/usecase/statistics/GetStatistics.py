from datetime import datetime, date, timedelta
import calendar
from data.appDataBase import get_all_reservation_by_date, get_all_rent_statics, get_all_rent_statics_categorie, get_all_reservation_by_categorie

def usecase_get_statistics_year(year, categorie):
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)
    return usecase_get_statistics(start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"), categorie)

def usecase_get_statistics_month(month, categorie):
    current_year = datetime.now().year
    start_date = date(current_year, month, 1)
    last_day = calendar.monthrange(current_year, month)[1]
    end_date = date(current_year, month, last_day)
    return usecase_get_statistics(start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"), categorie)

def usecase_get_statistics(start_date, end_date, categorie):

    if start_date != None and end_date != None:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        if (start > end):
            raise Exception("Fechas inconsistentes.")
    
    list_rent = []
    list_reservation = []

    if categorie != None:
        list_rent = get_all_rent_statics_categorie(categorie)
        list_reservation = get_all_reservation_by_categorie(start_date, end_date, categorie)
    else:    
        list_rent = get_all_rent_statics()
        list_reservation = get_all_reservation_by_date(start_date, end_date)


    if list_rent == None and list_reservation == None:
        raise Exception("No existen registros para las fechas, mes o año ingresado.")

    if start_date != None and end_date != None:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        list_rent = __stream__(list_rent, start, end)
        list_reservation =  __stream__(list_reservation, start, end)

    count = len(list_rent)
    dic_rent = { 
        "element_count" : count, 
        "total_value": 0.0, 
        "average": 0.0 , 
        "type": "rent"
    }

    count = len(list_reservation)
    dic_reservation = { 
        "element_count" : count, 
        "total_value": 0.0, 
        "average": 0.0 , 
        "type": "reservation"
    }

    count = len(list_rent) + len(list_reservation)
    dic_total = { 
        "element_count" : count, 
        "total_value": 0.0, 
        "average": 0.0 , 
        "type": "all"
    }


    __calculate__(dic_reservation, list_reservation)
    __calculate__(dic_rent, list_rent)

    if dic_total.get("element_count") == 0:
        avr = 0
    else:
        avr = (dic_rent.get("total_value") + dic_reservation.get("total_value")) / dic_total.get("element_count")
    dic_total.update({ "average": avr })
    total = dic_rent.get("total_value") + dic_reservation.get("total_value")
    dic_total.update({ "total_value": total })

    return { "rent": dic_rent, "reservation": dic_reservation, "total": dic_total }
    
def __calculate__(dic, list):
    total_value = 0.0
    for x in list:
        total_value += x.total_value
    dic.update({"total_value": total_value})
    if dic.get("element_count") == 0:
        avr = 0
    else:
        avr = (total_value/dic.get("element_count")) 
    dic.update({"average": avr})
    
def __stream__(list, start, end):
    print(list)
    aux = []
    for x in list:
        s = datetime.strptime(x.start_day, "%Y-%m-%d")
        e = datetime.strptime(x.end_day, "%Y-%m-%d")
        if start <= s and end >= e:
            aux.append(x)
    return aux
