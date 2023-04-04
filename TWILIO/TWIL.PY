import os
from twilio.rest import Client

sid = os.environ.get['TWILIO_SID']
token = os.environ.get['TWILIO_TOKEN']

cliente = Client(sid, token)
mensaje = cliente.messages.create(
    body="Hola, este es un mensaje de prueba",
    from_=os.environ.get['TWILIO_NUMBER'],
    to="+543415883040"
)