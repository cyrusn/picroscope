from gpiozero import Button, LED
from signal import pause

from send_email import Email
from picroscope import Picroscope

LED_PIN = 19
LEFT_BUTTON_PIN = 20
RIGHT_BUTTON_PIN = 21
GMAIL_USER = ""
GMAIL_PASSWORD = ""

led = LED(LED_PIN)
left_button = Button(LEFT_BUTTON_PIN)
right_button = Button(RIGHT_BUTTON_PIN)

# initiation`

picroscope = Picroscope(led=led, rotation=90, captureDir="/home/pi/Desktop/Images")
print(picroscope.help_text)

email = Email(GMAIL_USER, GMAIL_PASSWORD)
email.login()


def captureAndSendEmail():
    filename = picroscope.capture()
    if filename is not None:
        email.subject = "STEM 「語文」同樂日 - 顯微鏡DIY"
        recipient = input("Recipient: ")
        email.recipient = recipient
        email.add_attachment(filename)
        email.send()
        email.close()


left_button.when_pressed = picroscope.toggle_preview
right_button.when_pressed = captureAndSendEmail
pause()

