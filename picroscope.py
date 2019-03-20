#! /user/bin/env python3
from picamera import PiCamera
from datetime import datetime
from os import path


class StubLED:
    def on(self):
        pass

    def off(self):
        pass


class Picroscope:
    def __init__(self, led=None, rotation=0, captureDir="/home/pi/Desktop"):
        self.captureDir = captureDir
        self.led = led if led else StubLED()
        self.camera = PiCamera()
        self.camera.rotation = rotation
        self.preview = False

    def capture(self):
        if self.preview:
            now = datetime.now().isoformat()
            file = path.join(self.captureDir, format(now) + ".jpg")
            print("Image Captured: ", file)
            self.camera.capture(file)
            return file
        return None

    def toggle_preview(self):
        self.preview = not self.preview
        if self.preview:
            self.led.on()
            self.camera.start_preview()
        else:
            self.led.off()
            self.camera.stop_preview()

    @property
    def help_text(self):
        return (
            "Press left button to start preview.\n"
            + "Press right button while previewing to capture image.\n"
            + "Press ctrl-C to stop the programme."
        )
