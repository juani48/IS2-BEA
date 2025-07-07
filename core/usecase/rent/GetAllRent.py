from data.appDataBase import get_all_rent_by_date

def usecase_get_all_rent():
    list = get_all_rent_by_date(None, None)
    return [x.json() for x in list]