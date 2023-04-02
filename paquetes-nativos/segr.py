from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
mensaje = MIMEMultipart()
mensaje["From"] = "hola"
mensaje["To"] = "hola@gmail.com"
mensaje["Subject"] = "Hola"
cuerpo = MIMEtext("Hola mundo")
mensaje.attach(cuerpo)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("", "")
    
               