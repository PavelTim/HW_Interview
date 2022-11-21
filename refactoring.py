import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Gmail:
    # Класс только для работы с gmail
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    # видимо это корпоративная почта, которую следует использовать всему персоналу по умолчанию
    def __init__(self, login='login@gmail.com', password='qwerty'):
        self.login = login                  # отправитель sender
        self.password = password


    def _sendmail(self, msg):
        ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client идентифицируем себя в клиенте smtp gmail
        ms.ehlo()
        # secure our email with tls encryption защитить нашу электронную почту с помощью шифрования tls
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, self.recipients, msg.as_string())
        ms.quit()
        # send end

    # класс по умолчанию спамит васе и пете бессмысленные сообщения
    def send_message(self, recipients=('vasya@email.com', 'petya@email.com'),
                     subject='Subject', message='Message'):
        self.subject = subject                  # тема сообщения
        self.recipients = recipients            # получатели
        self.message = message                  # сообщение

        # send message
        msg = MIMEMultipart()                       # создаем сообщение
        msg['From'] = self.login                    # отправитель
        msg['To'] = ', '.join(self.recipients)      # кому
        msg['Subject'] = self.subject               # тема сообщения
        msg.attach(MIMEText(self.message))          # добавляем текст в сообщение

        self._sendmail(msg)                         # связываемся в smtp gmail и отправляем письмо


    def recieve(self, header=None):
        # recieve получить письмо
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message
        #end recieve


if __name__ == '__main__':
    gmail = Gmail(login='login@gmail.com', password='qwerty')
    gmail.send_message(
        recipients=['vasya@email.com', 'petya@email.com'],
        subject='Subject', message='Message'
    )
    # безбашенный прием сообщений
    email_message = gmail.recieve()
    print(email_message)
    # работоспособность кода не проверялась