from data.appDataBase import change_password,get_user_by_email
from core.usecase.user.RequestUser import _random_password
from core.usecase.service import SendMail


def usecase_recover_password(email):
    localUser = get_user_by_email(email=email)
    if localUser is not None:
        newPassword = _random_password()
        change_password(dni=localUser.dni, password=newPassword)
        send_Mail_new_password(user=localUser)


def send_Mail_new_password(user):
    SendMail.usecase_send_mail(

        emailDest=user.email,
        subject="Nueva contraseña  - Bob El Alquilador",
        body = f"""
                ¡Hola {user.name}!

                Para mantener tu cuenta segura, hemos generado una contraseña temporal para acceder a Bob El Alquilador 🌟

                Tu nueva contraseña: {user.password}

                Puedes iniciar sesión ahora mismo y cambiarla fácilmente:
                1. Ingresa con esta contraseña temporal
                2. Ve a "{user.name}"
                3. Presiona "Editar perfil"
                3. Selecciona "Cambiar contraseña"

                ¿No fuiste tú? Por favor avísanos inmediatamente respondiendo este correo.

                Gracias por confiar en nosotros para cuidar de tus alquileres ¡Estamos aquí para ayudarte en lo que necesites!

                Saludos cordiales, El equipo de Bob El Alquilador 

                PS: Recuerda que tu seguridad es nuestra prioridad. Nunca te pediremos tu contraseña por correo.
                """
                )
