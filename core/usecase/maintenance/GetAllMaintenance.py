from data.appDataBase import get_all_maintenance

def usecase_get_all_maintenance():
    list = get_all_maintenance()
    return [x.json() for x in list]
