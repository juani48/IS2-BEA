from data.appDataBase import enable_employee, get_user

def usecase_enable_employee(dni):
    local_employee= get_user(dni)
    enable_employee(nro_employee= local_employee.employee_number)