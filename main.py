from gpiozero import Button, LED
from signal import pause

from send_email import Email
from picroscope import Picroscope
from email.utils import parseaddr

from constant import GMAIL_USER, GMAIL_PASSWORD

LED_PIN = 16
LEFT_BUTTON_PIN = 20
RIGHT_BUTTON_PIN = 21
CAPTURE_DIR = "/home/pi/Desktop/picroscope/images"


led = LED(LED_PIN)
left_button = Button(LEFT_BUTTON_PIN)
right_button = Button(RIGHT_BUTTON_PIN)

# initiation`

picroscope = Picroscope(led=led,captureDir=CAPTURE_DIR)
print(picroscope.help_text)

email = Email(GMAIL_USER, GMAIL_PASSWORD)
email.login()


def captureAndSendEmail():
    filename = picroscope.capture()
    if filename is not None:
        picroscope.toggle_preview()
        email.subject = "STEM 「語文」同樂日 - 顯微鏡DIY"
        recipient = input("Recipient: ")
        address = parseaddr(recipient)
        print(address)
#        if address[1] != "":
#            email.recipient = recipient
#            email.add_attachment(filename)
#            email.send()

left_button.when_pressed = picroscope.toggle_preview
right_button.when_pressed = captureAndSendEmail
pause()
