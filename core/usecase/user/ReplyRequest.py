from data.appDataBase import enable_user,delete_user,get_user
from data.model.UserModel import UserModel
from core.usecase.service import SendMail


def usecase_reply_request(reply,dni):
    localUser = get_user(dni=dni)
    if (reply):
        enable_user(dni=dni)        
        send_Mail_Request_Acepted(user=localUser)
        return "Solicitud aceptada"
    else:
        delete_user(dni=dni)
        send_Mail_Request_Rejected(user=localUser)
        return "Solicitud rechazada"


def send_Mail_Request_Acepted(user):
    SendMail.usecase_send_mail(

        emailDest=user.email,
        subject="Solicitud aceptada - Bob El Alquilador",
        body= f"""
                Hola {user.name} {user.lastname},

                    ¡Bienvenido a Bob El Alquilador!

                        Nos alegra tenerte con nosotros. A continuación, te compartimos tu contraseña temporal para que puedas iniciar sesión en nuestro sistema. Recuerda que puedes cambiarla en cualquier momento desde tu perfil:

                            🔐 Contraseña: {user.password}

                    Si tienes alguna duda o necesitas ayuda, no dudes en contactarnos.

                    Gracias por confiar en nosotros.

                    Saludos cordiales,  
                    Sistema de Gestión BEA
                    """

    )

def send_Mail_Request_Rejected(user):
    SendMail.usecase_send_mail(

        emailDest=user.email,
        subject="Solicitud rechazada - Bob El Alquilador",
        body=f"""
                Hola {user.name} {user.lastname},

                    Gracias por tu interés en formar parte de Bob El Alquilador.

                        Lamentamos informarte que no hemos podido aprobar tu solicitud debido a que los datos proporcionados no coinciden con el número de DNI registrado.

                    Te invitamos a revisar la información ingresada y, si lo deseas, volver a postularte con los datos correctos.

                    Si tienes alguna duda o requerís asistencia, no dudes en comunicarte con nosotros.

                    Te deseamos mucho éxito.

                    Saludos cordiales,  
                    Sistema de Gestión BEA
                    """
    )
