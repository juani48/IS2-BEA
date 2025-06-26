from data.appDataBase import get_all_commentarys

def usecase_get_all_commentarys(machine_patent):
    list = get_all_commentarys(machine_patent)
    return [ x.json() for x in list ]