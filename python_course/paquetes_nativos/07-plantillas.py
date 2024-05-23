from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
from string import Template



plantilla = Path("python_course/paquetes_nativos/plantilla.html").read_text("utf-8")

template = Template(plantilla)

cuerpo = template.substitute(usuario = "Chanchito Alegre y Contento")
# cuerpo = template.substitute({"usuaio" : "Chanchito Feliz"})





path = Path("python_course/paquetes_nativos/imagen_prueba.png")

mime_image = MIMEImage(path.read_bytes())

mensaje = MIMEMultipart()

mensaje["from"] = "juancar2805@gmail.com"

mensaje["to"] = "juancar2805@gmail.com"

mensaje["subject"] = "Esta es una Prueba"

cuerpo = MIMEText(cuerpo, "html")

mensaje.attach(cuerpo)

mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login("juancar2805@gmail.com", "Password")

    smtp.send_message(mensaje)
