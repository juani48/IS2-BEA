from data.model.UserModel import UserModel
from data.appDataBase import insert_employee
from core.usecase.user.RequestUser import _random_password
from core.usecase.service import SendMail
from data.query.get import query_get_user, query_get_employee, query_get_user_by_email, query_get_employee_by_number

def usecase_add_employee(dni, email, name, lastname, phone, dateBirth, employeeN):
    dni = int(dni)
    phone = int(phone)
    employeeN = int(employeeN)

    if query_get_user.execute(dni) is not None:
        raise ValueError("El DNI ya se encuentra registrado.")
    
    if query_get_employee.execute(employeeN=employeeN) is not None: 

        if query_get_employee.execute(employeeN=employeeN) or query_get_employee.execute(employeeN=employeeN * -1):
            raise ValueError("El número de empleado ya se encuentra registrado.")        
        
    if query_get_user_by_email.execute(email):
        raise ValueError("El correo ya se encuentra registrado.")

    if (_validator(dni, email, name, lastname)):        
        password = _random_password()
        user = UserModel(
                dni=int(dni),
                password= password,
                email= email,
                name= name,
                lastname= lastname,
                phone = phone,
                birth_date = dateBirth,
                employee_number= employeeN,
                type = "Empleado",
                authorized = True
            )
        insert_employee(
            dni,
            user,
        )
        sendMailEmployee(email=email,name=name,lastname=lastname,password=password)

    return True

def _validator(dni, email, name, lastname):
    if dni == "":
        raise Exception("El DNI no puede estar vacío")
    if email == "":
        raise Exception("El mail  no puede estar vacío")
    if name == "":
        raise Exception("El nombre  no puede estar vacío")
    if lastname == "":
        raise Exception("El apellido  no puede estar vacío")
    return True
    
def sendMailEmployee(email,name,lastname,password):
    SendMail.usecase_send_mail(
        emailDest=email,
        subject="Bienvenido al equipo de trabajo",
        body=f"""
            Hola {name}, {lastname}.

            Le damos la bienvenida al equipo de trabajo de Bob El Alquilador, a continuación le dejamos la contraseña para su inicio de sesión, recuerde que puede cambiarla cuando desee:
              {password}

            Gracias y saludos,
            Sistema de Gestión BEA
        """
    )