from datetime import datetime
from data.appDataBase import get_all_reservation_by_date, get_all_rent_by_date, get_all_rent_by_categoire, get_all_reservation_by_categorie

def usecase_get_statistics(start_date, end_date, categorie):
    
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    if (start > end):
        raise Exception("Fechas inconsistentes.")
    
    list_rent = []
    list_reservation = []

    if categorie != None or categorie != "":
        list_rent = get_all_rent_by_categoire(start_date, end_date, categorie)
        list_reservation = get_all_reservation_by_categorie(start_date, end_date, categorie)
    else:    
        list_rent = get_all_rent_by_date(start_date, end_date)
        list_reservation = get_all_reservation_by_date(start_date, end_date)

    print(list_rent)
    print(list_reservation)
       
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
    print(dic)
    