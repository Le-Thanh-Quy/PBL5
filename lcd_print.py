from rpi_lcd import LCD
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

lcd = LCD()

def lcd_print(content):
    try:
        lcd.text(content, 2)
    except KeyboardInterrupt:
        pass


def lcd_clear():
    try:
        lcd.clear()
        lcd.text("Safe - QTHV", 1)
    except KeyboardInterrupt:
        pass