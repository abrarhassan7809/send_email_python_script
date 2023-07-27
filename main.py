import smtplib
from email.mime.text import MIMEText


def send_email(host, port, subject, msg, sender, receiver, password):
    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(receiver)
    smtp_server = smtplib.SMTP_SSL(host, port)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, receiver, msg.as_string())

    smtp_server.quit()


def main(sender, receiver, app_password):
    host = "smtp.gmail.com"
    port = 535  # or 465

    user = sender
    pwd = app_password
    subject = "test email for messages"
    msg = f'Hi {receiver}'
    sender = user
    receivers = [receiver]

    send_email(host, port, subject, msg, sender, receivers, pwd)


if __name__ == '__main__':
    main('bdmsystm@gmail.com', 'abrarhassan7809@gmail.com', 'asim1234')
