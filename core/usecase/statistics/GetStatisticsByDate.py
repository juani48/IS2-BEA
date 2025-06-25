from datetime import datetime
from data.appDataBase import get_all_reservation_by_date, get_all_rent_by_date
from data.model.RentModel import RentModel

def usecase_get_statistics(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    if (start > end):
        raise Exception("Fechas inconsistentes.")
    
    list_rent = get_all_rent_by_date(start_date, end_date)
    list_reservation = get_all_reservation_by_date(start_date, end_date)

    dic_rent = { 
        "element_count" : len(list_rent), 
        "total_value": 0.0, 
        "average": 0.0 , 
        "type": "rent"
    }

    dic_reservation = { 
        "element_count" : len(list_reservation), 
        "total_value": 0.0, 
        #"average_shipment" : 0.0 ,
        "average": 0.0 , 
        "type": "reservation"
    }

    dic_total = { 
        "element_count" : (dic_rent.get("element_count")+dic_reservation.get("element_count")), 
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
    dic.get("total_value") = total_value
    dic.get("average") = total_value/dic.get("element_count")
    