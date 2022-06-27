import RPi.GPIO as GPIO
from rpi_lcd import LCD
from gpiozero import AngularServo

servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)

servo.angle = 90

