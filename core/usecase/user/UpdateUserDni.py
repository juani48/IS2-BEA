from data.appDataBase import update_user_dni

def usecase_update_user_dni(dni, new_dni):
    if(new_dni == None or new_dni == 0 ):
        raise Exception("El campo dni no puede estar vacio")
    update_user_dni(dni, new_dni)