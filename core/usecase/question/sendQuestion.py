from core.usecase.service import SendMail
from data.appDataBase import get_user_by_email

def usecase_send_question(emailUser,name,lastname,question):
    local_admin= get_user_by_email("bobelalquilador@gmail.com")
    SendMail.usecase_send_mail(
        emailDest="bobelalquilador@gmail.com",
        subject="Nueva pregunta registrada",
        body=f"""
            Hola {local_admin.name}, {local_admin.lastname}.

            Le informamos que recibió una nueva pregunta de parte de { name }, {lastname}.
              A continuación se la informamos:
              {question}
            
            El correo del usuario es: {emailUser}

            Saludos,
            Sistema de Gestión BEA
        """
    )