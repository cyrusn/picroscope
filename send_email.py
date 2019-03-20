import smtplib
from email.message import EmailMessage

import getpass

SMTP = "smtp.gmail.com"
SMTP_PORT = 587


class Email:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.message = EmailMessage()
        self.sender = username

        self.message["From"] = self.sender

    def login(self):
        try:
            self.server = smtplib.SMTP(SMTP, SMTP_PORT)
            self.server.ehlo()
            self.server.starttls()
            self.server.login(self.username, self.password)
            print("Successful login")
        except smtplib.SMTPAuthenticationError:
            print("Invalid login credential")
            exit()

    @property
    def subject(self):
        return self.message["Subject"]

    @subject.setter
    def subject(self, subject):
        self.message["Subject"] = subject

    @property
    def recipient(self):
        return self.message["To"]

    @recipient.setter
    def recipient(self, recipient):
        self.message["To"] = recipient

    def add_attachment(self, filename):
        with open(filename, "rb") as fp:
            img_data = fp.read()
            self.message.add_attachment(
                img_data, maintype="image", subtype="png", filename=filename
            )
            fp.close()

    def send(self):
        self.server.send_message(self.message)
        print("Message is sent successfully.")

    def close(self):
        self.server.close()

