from data.appDataBase import change_password,get_user


def usecase_change_password (dni,password_Act, password_New_1 , password_New_2):
    
    if (password_Act == get_user(dni)):

        if (len(password_New_1) < 8 and len(password_New_2) < 8):

            if (password_New_1 == password_New_2):
                change_password(dni,password_New_1)
            else:
                raise Exception("Las nuevas contraseñas no coinciden")
            
        else:            
            raise Exception("Ingrese al menos 8 caracteres")
        
    else:
        raise Exception("Contraseña actual incorrecta")
    