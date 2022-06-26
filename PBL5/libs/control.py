from gpiozero import AngularServo
from time import sleep
from threading import Thread
import RPi.GPIO as GPIO


isDoorOpen = False
class control(Thread):
    def __init__(self, serial):
        super(control, self).__init__()
        self.serial = serial
        self.ir_pin = 40
        self.time_wait = 5
        self.servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.ir_pin, GPIO.IN)

    def run(self):
        while (True):
            if isDoorOpen:
                print(GPIO.input(self.ir_pin))
                if GPIO.input(self.ir_pin) == 0:
                    isClosingConfirm = True
                    for i in range(self.time_wait):
                        sleep(1)
                        if (GPIO.input(self.ir_pin) == 1):
                            isClosingConfirm = False
                            break
                        if isClosingConfirm:
                            self.controlServo(angle=-90)

    def controlServo(self, angle):
        self.servo.angle = angle
