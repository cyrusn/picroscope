from smtplib import SMTP, SMTPAuthenticationError


class Server:
    def __init__(self, smtp, port):
        self.server = SMTP(smtp, port)

    def login(self, username, password):
        try:
            self.server.ehlo()
            self.server.starttls()
            self.server.login(username, password)
            self.username = username
            print("Successful login")
        except SMTPAuthenticationError:
            print("Invalid login credential")
            exit()
            
    def send_message(self, message):
        self.server.send_message(message)

    def close(self):
        self.server.close()
