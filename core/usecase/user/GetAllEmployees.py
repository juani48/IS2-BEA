from data.query.get_all import query_get_all_employees


def usecase_get_all_employees():
    employees_list = query_get_all_employees.execute()
    return [ x.json() for x in employees_list ]
     