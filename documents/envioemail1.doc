# Envio de e-mail com anexo
# https://www.youtube.com/watch?v=umvzsQLZYD4

import smtplib

# PADRONIZAÇÃO ESTRUTRA DADOS FORMATO MIME E-MAIL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# binário para anexar um arquivo 
from email.mime.base import MIMEBase
from email import encoders

# S M T P - Simple Mail transfer protocol
# para criar o servidor e enviar o e-mail

# 1 - STARTAR O SERVIDOR SMTP
host = "smtp.gmail.com"
port = "587"
login = "roeland.e.janssen@gmail.com"
senha = "ljfgxlwkvdyokxjh"

server = smtplib.SMTP(host,port)

server.ehlo()
server.starttls()

server.login(login,senha)

#2 - CONSTRUIR O E-MAIL TIPO MIME
corpo = "<b>Olá, Tudo bem?</b>"

# montando e-mail
email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = login
email_msg['Subject'] = "Meu e-mail enviado por Roeland"
email_msg.attach(MIMEText(corpo, 'html'))
#email_msg.attach(MIMEText(corpo, 'Plain'))

# abrimos o arquivo em modo leitura e binary
cam_arquivo = "C:\Roeland\Principal\Projetos\Site\projeto-video\EnviarEmail.py"
attachment = open(cam_arquivo, 'rb')

# lemos o arquivo no modo binário e jogamos codificado em base 64 (que é o que e-mail precisa)
att = MIMEBase('application', 'octed-stream')
att.set_payload(attachment.read())
encoders.encode_base64(att)

# adicionamos o cabeçalho no tipo anexo do e-mail
att.add_header('Content-Disposition', f'attachment; filename = EnviarEmail.py')
#att.add_header('Content-Disposition', f'attachment; filename = {nomearquivo}')


# fechamos o arquivo
attachment.close()

# colocamos o anexo no corpo do e-mail
email_msg.attach(att)

#3 - ENVIAR o E-MAIL tipo MIME no SERVIDOR SMTP
server.sendmail(email_msg["From"], email_msg["To"], email_msg.as_string())
server.quit()