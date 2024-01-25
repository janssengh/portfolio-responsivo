import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>Olá Roeland, boa tarde !</p>
    <p>Envio de e-mail automático pelo meu app para teste! Favor exclua o mesmo !</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "e-mail envio teste"
    msg['From'] = 'roeland.e.janssen@gmail.com'
    msg['To'] = 'roeland.e.janssen@gmail.com'
    password = 'howwfoakvbxicalm' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()