from gpiozero import AngularServo
from time import sleep
from lcd_print import lcd_print, lcd_clear
from threading import Thread
from firebase_admin import db
import RPi.GPIO as GPIO


isDoorOpen = False
class control(Thread):
    def __init__(self, serial):
        super(control, self).__init__()
        self.serial = serial
        self.ir_pin = 40
        self.time_wait = 5
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.ir_pin, GPIO.IN)
        self.servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)


    def run(self):
        self.controlServo(angle=90)
        while (True):
            if isDoorOpen:
                self.controlServo(angle=40)
                lcd_print("Opening...")
                if GPIO.input(self.ir_pin) == 0:
                    isClosingConfirm = True
                    for i in range(self.time_wait):
                        lcd_print(str(self.time_wait - i))
                        sleep(1)
                        if (GPIO.input(self.ir_pin) == 1):
                            isClosingConfirm = False
                            break
                    if isClosingConfirm:
                        db.reference("/Safes/").child(self.serial).child("isOpen").set(False)
                        db.reference("/Safes/").child(self.serial).child("faceVerification").set("None")
                        self.controlServo(angle=90)
                        lcd_print("Closing...")
                        sleep(1)
                        lcd_print("Closed")
                        sleep(1)
                        lcd_clear()

    def controlServo(self, angle):
        self.servo.angle = angle

