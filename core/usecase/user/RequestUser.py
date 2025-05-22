from core.usecase.service import SendMail
from core.usecase.user import Signin
from data.appDataBase import get_user
from datetime import datetime, date
import secrets
import string

def usecase_request_user(dni, email, name, lastname, phone, birthDate, terms_accepted):
    _validator(dni, email, name, lastname, birthDate, 18, terms_accepted)

    dni_str = str(dni)

    user_by_dni = get_user(dni, "")
    if user_by_dni is not None:
        raise Exception("DNI ya registrado")

    user_by_email = get_user(0, email)
    if user_by_email is not None:
        raise Exception("Email ya registrado")

    SendMail.usecase_send_mail(
        emailDest=email,
        subject="Solicitud de registro",
        body=f"""
            Hola equipo,

            Se ha recibido una nueva solicitud de registro por parte de un usuario con DNI: {dni_str}

            Por favor, ingrese al sistema para revisar y aprobar o rechazar el registro según corresponda.

            Gracias y saludos,
            Sistema de Gestión BEA
        """
    )

    password = _random_password()

    Signin.usecase_signing(dni, password, email, name, lastname, phone)

    return True

def _validator(dni, email, name, lastname, birth_date_str, minimum_age, terms_accepted):
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

    if not terms_accepted:
        raise Exception("Debes aceptar los términos y condiciones para continuar")

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
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(caracteres) for _ in range(longitud))