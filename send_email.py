from email.message import EmailMessage
from os import path

import getpass


class Email:
    def __init__(self, server):
        self.server = server
        self.message = EmailMessage()
        self.message["From"] = server.username

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
                img_data,
                maintype="image",
                subtype="png",
                filename=path.basename(filename),
            )
            fp.close()

    def send(self):
        self.server.send_message(self.message)
        print("Image is sent successfully to {}.".format(self.recipient))
