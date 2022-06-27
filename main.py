from recognition import PhatHienVaLayDuLieuKhuonMat, NhanDien
from firebase_admin import db
from lcd_print import lcd_print, lcd_clear
from libs import running, control
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import time
import RPi.GPIO as GPIO




GPIO.setmode(GPIO.BOARD)             
whistle_pin = 38
GPIO.setup(whistle_pin, GPIO.OUT)   
SERIAL = "111111111111111"
threadRecognition = running
threadControl = control
threadRunning = False
isRunning = False
public_url = ""
bucket = storage.bucket()


def listener_training_image_chage(event):
    global threadRunning, public_url
    if event.data == public_url:
        db.reference(
                    "/Safes/").child(SERIAL).child("training").child("state").set("No")
        threadRecognition.isRuning = threadRunning
        lcd_clear()
        lcd_print("Complete...")
        lcd_clear()

def listener_training_event(event):
    global threadRunning, public_url, bucket
    if event.data == "Yes":
        threadRunning = threadRecognition.isRuning
        threadRecognition.isRuning = False
        lcd_clear()
        lcd_print("3")
        time.sleep(1)
        lcd_print("2")
        time.sleep(1)
        lcd_print("1")
        time.sleep(1)
        lcd_print("Training...0%")
        time_now = round(time.time() * 1000)
        is_complete = PhatHienVaLayDuLieuKhuonMat.start_recognize_and_training(
            SERIAL)
        if is_complete:
            blob = bucket.blob("Face/Training/" + str(time_now) + 
                               ".JPG")
            blob.upload_from_filename("/home/qthv/Desktop/PBL5/recognition/DuLieuKhuonMat/" + SERIAL + "/pic5.png")
            blob.make_public()
            public_url = blob.public_url
            db.reference(
                "/Safes/").child(SERIAL).child("training").child("image").set(blob.public_url)
            db.reference(
                "/Safes/").child(SERIAL).child("training").child("image").listen(listener_training_image_chage)

def listener_recognition_event(event):
    global isRunning
    threadRecognition.isRuning = event.data
    threadRecognition.isStart = event.data
    if not isRunning:
        isRunning = True
        threadRecognition.running(SERIAL, db.reference("/Safes/").child(SERIAL).child("phone").get()).start()
                
def listener_door_open_event(event):
    threadControl.isDoorOpen = event.data

def listener_door_close_event(event):
    global whistle_pin
    GPIO.output(whistle_pin, 0)
    if event.data == "None":
        threadRecognition.isRuning = True
    elif event.data == "False":
        GPIO.output(whistle_pin, 1)


if __name__ == "__main__":
    lcd_clear()
    db.reference("/Safes/").child(SERIAL).child(
        "training").child("state").listen(listener_training_event)
    db.reference("/Safes/").child(SERIAL).child(
        "isStart").listen(listener_recognition_event)
    db.reference("/Safes/").child(SERIAL).child(
        "isOpen").listen(listener_door_open_event)
    db.reference("/Safes/").child(SERIAL).child(
    "faceVerification").listen(listener_door_close_event)
    threadControl.control(SERIAL).start()
