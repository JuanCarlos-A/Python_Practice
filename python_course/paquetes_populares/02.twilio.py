from twilio.rest import Client
import os

sid = os.environ.get("TWILIO_SID")
token = os.environ.get("TWILIO_TOKEN")
phone_number = os.environ.get("TWILIO_PHONE")


cliente = Client(sid, token)

mensaje = cliente.messages.create(
    body="Hola Juan, soy un sms",
    from_=phone_number,
    to="+573012368606"
)
