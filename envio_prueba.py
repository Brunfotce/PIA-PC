import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def Enviar_Correo():
    port = 587  
    subject = "Enviar Excel Cifrado"
    body = "PIA"
    smtp_server = "smtp.office365.com"
    remitente = "vanessa.alvaradoe@uanl.edu.mx"
    password = "Vanessa200818"
    destinatario="alvarado.e.vanessa@gmail.com"
    
    envio = MIMEMultipart()
    envio["From"] = remitente
    envio["To"] = destinatario
    envio["Bcc"] = destinatario
    envio["Subject"] = subject
    envio.attach(MIMEText(body, "plain"))

    filename = ["reporte_analizador_urls_encriptado.csv"]

    for i in filename:

        with open(i, "rb") as attachment:
            
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

         
        encoders.encode_base64(part)

       
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {i}",
        )


        envio.attach(part)
        text = envio.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(remitente, password)
        server.sendmail(remitente, destinatario, text)
