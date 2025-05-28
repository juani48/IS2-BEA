from core.usecase.service import SendMail
from core.usecase.user import Signin
from data.model.UserModel import UserModel
from data.appDataBase import insert_user,get_all_employees
from datetime import datetime, date
import secrets
import string
import bcrypt

def usecase_request_user(dni, email, name, lastname, phone, birthDate):
    _validator(dni, email, name, lastname, birthDate, 18)

    password = _random_password()

    user = UserModel(
        dni=dni,
        password=password,
        email=email,
        name=name,
        lastname=lastname,        
        birth_date=birthDate,
        phone=phone,
        type = "Cliente"
    )
    insert_user(dni=dni,user=user,email=email)
    sendMailEmployees(dni=dni)
    sendMailUser(email=email,name=name,lastname=lastname)
    

def _validator(dni, email, name, lastname, birth_date_str, minimum_age):
    required_fields = {
        "DNI": dni,
        "mail": email,
        "nombre": name,
        "apellido": lastname,
        "fecha de nacimiento": birth_date_str
    }

    # Validación de campos vacíos
    for field_name, value in required_fields.items():
        if not value:
            raise Exception(f"El campo '{field_name}' no puede estar vacío")

    # Validación de formato de fecha y edad
    try:
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
    except ValueError:
        raise Exception("El formato de la fecha de nacimiento es inválido. Usa YYYY-MM-DD")

    if birth_date > date.today():
        raise Exception("La fecha de nacimiento no puede ser futura")

    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    if age < minimum_age:
        raise Exception(f"El usuario debe tener al menos {minimum_age} años")
    
def _random_password(longitud=12):
    caracteres = string.ascii_letters + string.digits + "."  # solo letras, dígitos y punto
    return ''.join(secrets.choice(caracteres) for _ in range(longitud))

def sendMailUser(email,name,lastname):
    SendMail.usecase_send_mail(
        emailDest=email,
        subject="Solicitud enviada - Bob el Alquilador",
        body=f"""
                Hola {name} {lastname},

                ¡Bienvenido/a a Bob El Alquilador!

                Gracias por registrarse con nosotros. Su solicitud ha sido recibida y se encuentra actualmente pendiente de confirmación. 
                    En cuanto sea aprobada, le notificaremos para que pueda acceder al sistema y comenzar a disfrutar de nuestros servicios.

                Agradecemos su confianza.

                Saludos cordiales,  
                Sistema de Gestión BEA
                """
    )

def sendMailEmployees(dni):
    empleados = get_all_employees()
    dni_str = str(dni)
    for empleado in empleados:
        SendMail.usecase_send_mail(
            emailDest=empleado.email,
            subject="Solicitud de registro",
            body=f"""
                Hola equipo,

                    Se ha recibido una nueva solicitud de registro por parte de un usuario con DNI: {dni_str}

                    Por favor, ingrese al sistema para revisar y aprobar o rechazar el registro según corresponda.

                    Gracias y saludos,
                    Sistema de Gestión BEA
            """
        )