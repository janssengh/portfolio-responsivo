from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from config import email, senha

import smtplib
import email.message

app = Flask(__name__)
app.secret_key = 'roeland'

def enviar_email(corpo_email, assunto, destinatario, remetente):  
    
    corpo_email = corpo_email
    msg = email.message.Message()
    msg['Subject'] = assunto
    msg['From'] = remetente
    msg['To'] = destinatario
    password = senha

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

mail_settings = {
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha
}

app.config.update(mail_settings)

class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )

        corpo_email = f'''
                        {formContato.nome} com o e-mail {formContato.email},
                        te envou a seguinte mensagem:

                        {formContato.mensagem}

                        '''
        assunto = f'{formContato.nome} te enviou uma mensagem no portfólio'
        destinatario = 'roeland.e.janssen@gmail.com'
        remetente = request.form["email"]
        
        enviar_email(corpo_email,assunto,destinatario,remetente)
        
        flash('Mensagem enviada com sucesso!')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)