import logging

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mailer(object):
    def __init__(self, username, password, smtp_address='smtp.unimelb.edu.au', smtp_port=587, logger=None):
        self.username = username
        self.password = password
        self.smtp_address = smtp_address
        self.smtp_port = smtp_port

        self.logger = logger or logging.getLogger(__name__)

        self._connect_to_server()

    def _connect_to_server(self):
        self.server = SMTP(self.smtp_address, self.smtp_port)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(self.username, self.password)

    def send(self, subject, body, to_address, from_address='student-it-noreply@unimelb.edu.au'):
        msg = MIMEMultipart('alternative')

        msg['Subject'] = subject
        msg['From'] = from_address
        msg['To'] = ', '.join(to_address)
        msg.attach(MIMEText(body, 'html'))

        self.server.sendmail(from_address, to_address, msg.as_string())
