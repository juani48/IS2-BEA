from data.appDataBase import get_all_commentarys

def usecase_get_all_commentarys(machine_number):
    list = get_all_commentarys(machine_number)
    return [ x.json() for x in list ]