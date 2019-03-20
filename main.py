from gpiozero import Button, LED
from signal import pause
from smtplib import SMTPRecipientsRefused


from send_email import Email
from email_server import Server
from picroscope import Picroscope

SMTP = "smtp.gmail.com"
SMTP_PORT = 587

from constant import GMAIL_USER, GMAIL_PASSWORD

LED_PIN = 16
LEFT_BUTTON_PIN = 20
RIGHT_BUTTON_PIN = 21
CAPTURE_DIR = "/home/pi/Desktop/picroscope/images"
EMAIL_SUBJECT = "STEM 「語文」同樂日 -- 顯微鏡 DIY"


led = LED(LED_PIN)
left_button = Button(LEFT_BUTTON_PIN)
right_button = Button(RIGHT_BUTTON_PIN)


picroscope = Picroscope(led=led, captureDir=CAPTURE_DIR)
print(picroscope.help_text)

server = Server(SMTP, SMTP_PORT)
server.login(GMAIL_USER, GMAIL_PASSWORD)


def send_image():
    filename = picroscope.capture()
    if filename is not None:
        picroscope.toggle_preview()

        email = Email(server)
        email.subject = EMAIL_SUBJECT
        email.recipient = input("Recipient: ")
        email.add_attachment(filename)
        
        try:
            email.send()
        except SMTPRecipientsRefused:
            print('Invalid email address')

    print()

left_button.when_pressed = picroscope.toggle_preview
right_button.when_pressed = send_image
pause()
