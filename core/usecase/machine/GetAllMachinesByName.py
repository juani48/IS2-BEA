from data.appDataBase import get_all_machines

def usecase_get_all_machines_by(name):
    list = get_all_machines()
    if(name != ""):
        list = [x.include(name) for x in list]
    return list
