from data.appDataBase import get_all_machines_admin

def usecase_get_all_machines():
    list = get_all_machines_admin()
    return [ x.json() for x in list ]