from django.core.mail import EmailMessage


def daily_report_run():
    send_email()


def send_email():
    edu = 'Edu Fontes <eduramofo@gmail.com>'
    subject = 'Relatório Diário - Edu Fontes'
    body = 'Detalhes do Relatório'
    email_from = edu
    to = [edu]
    reply_to = ['Edu Fontes <eduramofo@gmail.com>']
    email = EmailMessage(subject, body, email_from, to, reply_to=reply_to)
    email.send()
