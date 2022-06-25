from recognition import PhatHienVaLayDuLieuKhuonMat, NhanDien
from firebase_admin import db
import lcd_print
import firebase_admin
from firebase_admin import credentials
from firebase_admin import credentials
from firebase_admin import storage
import time


SERIAL = "111111111111111"
cred = credentials.Certificate(
    'C:\\Users\\ADMIN\\Desktop\\DoAN\\PBL5\\serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pi3b-162b7-default-rtdb.asia-southeast1.firebasedatabase.app/',
    'storageBucket': 'pi3b-162b7.appspot.com'
})


def lcd_print(content, delay):
    time.sleep(delay)
    print(content)

def listener_training_image_chage(event):
    db.reference(
                "/Safes/").child(SERIAL).child("training").child("state").set("No")

def listener_training_event(event):
    if event.data == "Yes":
        lcd_print("3", 1)
        lcd_print("2", 1)
        lcd_print("1", 1)
        lcd_print("Training...0%", 0)
        is_complete, url_image = PhatHienVaLayDuLieuKhuonMat.start_recognize_and_training(
            SERIAL)
        if is_complete:
            lcd_print("Training...100%", 0)
            lcd_print("", 0)
            bucket = storage.bucket()
            blob = bucket.blob("Face/Training/" + str(round(time.time() * 1000)) + 
                               ".JPG")
            blob.upload_from_filename(url_image)
            blob.make_public()
            db.reference(
                "/Safes/").child(SERIAL).child("training").child("image").set(blob.public_url)
            db.reference(
                "/Safes/").child(SERIAL).child("training").child("image").listen(listener_training_image_chage)
                


if __name__ == "__main__":
    db.reference("/Safes/").child(SERIAL).child(
        "training").child("state").listen(listener_training_event)
    # NhanDien.start_face_recognition()
