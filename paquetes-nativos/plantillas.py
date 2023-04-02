from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

plantilla = Path("plantilla.html").read_text()






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
    
               