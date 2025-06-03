from data.appDataBase import get_all_disable_employees

def usecase_get_all_employees():
    employees_list = get_all_disable_employees()
    return [ x.json() for x in employees_list ]
     