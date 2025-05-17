from core.usecase.user import SendMail

def usecase_request_user(dni,email):

    


    dniStr= str(dni)
    SendMail.usecase_send_mail(
        emailDest= email,
        subject= "Solicitud de registro",
        body=  f"""\
                    Hola equipo,

                    Se ha recibido una nueva solicitud de registro por parte de un usuario con DNI: 
        
                    {dniStr}

                    Por favor, ingresen al sistema para revisar y aprobar o rechazar el registro según corresponda.

                    Gracias y saludos,
                    Sistema de Gestión BEA
                """
    )

    ## agregar solicitud a la base de datos.

    return True