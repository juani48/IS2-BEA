from data.appDataBase import get_history_employee


def usecase_get_history_employee(empN):

    return get_history_employee(employee_number = empN)