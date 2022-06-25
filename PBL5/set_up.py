import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from firebase_admin import credentials
from firebase_admin import storage


cred = credentials.Certificate(
    'C:\\Users\\ADMIN\\Desktop\\DoAN\\PBL5\\serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pi3b-162b7-default-rtdb.asia-southeast1.firebasedatabase.app/',
    'storageBucket': 'pi3b-162b7.appspot.com'
})


def set_up(SERIAL, phone_number, pin):
    db.reference(
        "/Safes/").child(SERIAL).child("faceVerification").set("None")
    db.reference(
        "/Safes/").child(SERIAL).child("isOpen").set(False)
    db.reference(
        "/Safes/").child(SERIAL).child("isStart").set(False)
    db.reference(
        "/Safes/").child(SERIAL).child("training").child("state").set("No")
    db.reference(
        "/Safes/").child(SERIAL).child("wrong").child("timeLock").set("None")
    db.reference(
        "/Safes/").child(SERIAL).child("wrong").child("times").set(3)
    db.reference(
        "/Safes/").child(SERIAL).child("phone").set(phone_number)
    db.reference(
        "/Users/").child(phone_number).child("serial").set(SERIAL)
    db.reference(
        "/Users/").child(phone_number).child("isFirst").set(True)
    db.reference(
        "/Users/").child(phone_number).child("pinVerify").set(pin)


# set_up("QTHVPBL02072022", "+84384933379", "0123456789")


set_up("111111111111111", "+84343440509", "1111111111")