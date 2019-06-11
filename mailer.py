import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mailer:
    def __init__(self, to_address=None, message=None):
        self.from_address = 'info@theshadowfashion.com'
        self.to_address = to_address
        self.message = message
        self.send_email_to_client()

    def send_email_to_client(self):
        msg = MIMEMultipart()
        msg.set_unixfrom('author')
        msg['From'] = self.from_address
        msg['To'] = self.to_address
        msg['Subject'] = 'simple email in python'
        message = self.message
        msg.attach(MIMEText(message))

        mail_server = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
        mail_server.ehlo()
        mail_server.login('info@theshadowfashion.com', 'Sh@d0w123')

        try:
            mail_server.sendmail(self.from_address, self.to_address, msg.as_string())
        except Exception:
            pass
        finally:
            mail_server.quit()

