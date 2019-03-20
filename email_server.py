import smtplib


class Server:
    def __init__(self, smtp, port):
        self.server = smtplib.SMTP(smtp, port)

    def login(self, username, password):
        try:
            self.server.ehlo()
            self.server.starttls()
            self.server.login(username, password)
            self.username = username
            print("Successful login")
        except smtplib.SMTPAuthenticationError:
            print("Invalid login credential")
            exit()

    def close(self):
        self.server.close()
