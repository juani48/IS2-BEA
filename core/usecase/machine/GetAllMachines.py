from data.appDataBase import get_all_machines

def usecase_get_all_machines():
    list = get_all_machines()
    return [ x.json() for x in list ]