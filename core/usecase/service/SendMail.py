from email.message import EmailMessage
import ssl
import smtplib
import os
from dotenv import load_dotenv

def usecase_send_mail(emailDest,subject,body):
    # Cargar variables de entorno desde .env
    load_dotenv()

    # guardo mail emisor y receptor
    emailSender = "bobelalquilador@gmail.com"
    emailReciver= emailDest
    password = os.getenv("EMAIL_PASSWORD")

    # creo en Em todo el mail
    em= EmailMessage() 
    em ["From"] = emailSender
    em ["To"] = emailReciver
    em ["Subject"] = subject
    em.set_content(body)

    # encripto (?)
    context = ssl.create_default_context()

    # para mandarlo: primero desde donde(host gmail), 465=puerto, context es el SSL
    # despues en login inicio sesión con bobelalquilador@gmail.com despues
    # importante poner el em.as_string() sino se mana caracteres inentendibles
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
        smtp.login(emailSender,password)
        smtp.sendmail(emailSender,emailReciver, em.as_string())
    return True
