from data.appDataBase import change_password,get_user_by_email
from core.usecase.user.RequestUser import _random_password
from core.usecase.service import SendMail


def usecase_recover_password(emailUser):
    localUser= get_user_by_email(email=emailUser)
    if (localUser is not None):
        newPassword= _random_password()
        change_password(dni= localUser.dni,password=newPassword)
        send_Mail_new_password(user=localUser)


def send_Mail_new_password(user):
    SendMail.usecase_send_mail(

        emailDest=user.email,
        subject="Nueva contraseña  - Bob El Alquilador",
        body = f"""
                Hola {user.name} {user.lastname},

                    Se ha generado una nueva contraseña para tu cuenta en Bob El Alquilador.

                    A continuación, te compartimos tu nueva contraseña temporal para que puedas iniciar sesión en nuestro sistema.
                      Recuerda que puedes cambiarla en cualquier momento desde tu perfil:

                        🔐 Nueva contraseña: {user.password}

                Si no solicitaste este cambio o necesitas ayuda, por favor contáctanos de inmediato.

                Gracias por seguir confiando en nosotros.

                Saludos cordiales,  
                Sistema de Gestión BEA
"""

    )
