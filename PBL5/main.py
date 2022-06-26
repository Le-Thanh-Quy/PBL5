from recognition import PhatHienVaLayDuLieuKhuonMat, NhanDien
from firebase_admin import db
import lcd_print
from libs import running
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import time


SERIAL = "111111111111111"
threadRecognition = running
threadRunning = False
isRunning = False
public_url = ""
bucket = storage.bucket()

def lcd_print(content, delay):
    time.sleep(delay)
    print(content)

def listener_training_image_chage(event):
    global threadRunning, public_url
    if event.data == public_url:
        db.reference(
                    "/Safes/").child(SERIAL).child("training").child("state").set("No")
        threadRecognition.isRuning = threadRunning

def listener_training_event(event):
    global threadRunning, public_url, bucket
    if event.data == "Yes":
        threadRunning = threadRecognition.isRuning
        threadRecognition.isRuning = False
        lcd_print("3", 1)
        lcd_print("2", 1)
        lcd_print("1", 1)
        lcd_print("Training...0%", 0)
        time_now = round(time.time() * 1000)
        is_complete = PhatHienVaLayDuLieuKhuonMat.start_recognize_and_training(
            SERIAL)
        if is_complete:
            lcd_print("Training...100%", 0)
            lcd_print("", 0)
            blob = bucket.blob("Face/Training/" + str(time_now) + 
                               ".JPG")
            blob.upload_from_filename("C:\\Users\\ADMIN\\Desktop\\DoAN\\Code\\PBL5\\recognition\\DuLieuKhuonMat\\" + SERIAL + "\\pic5.png")
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
                


if __name__ == "__main__":
    db.reference("/Safes/").child(SERIAL).child(
        "training").child("state").listen(listener_training_event)
    db.reference("/Safes/").child(SERIAL).child(
        "isStart").listen(listener_recognition_event)
