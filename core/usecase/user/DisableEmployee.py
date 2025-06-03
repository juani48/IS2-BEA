from data.appDataBase import disable_employee,get_user

def usecase_disable_employee(dni):
    local_employee= get_user(dni)
    disable_employee(nro_employee= local_employee.employee_number)