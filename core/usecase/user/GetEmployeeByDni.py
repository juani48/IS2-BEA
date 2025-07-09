from data.appDataBase import get_user

def usecase_get_employee_by_dni(dni):
    local_user= get_user(dni= dni)
    if (local_user is not None):
        if (local_user.employee_number != 0):
            return local_user
            
    return None