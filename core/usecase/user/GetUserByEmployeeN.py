from data.appDataBase import get_employee


def usecase_case_get_user_by_employee_number(empN):
    return get_employee(employeeN= empN)