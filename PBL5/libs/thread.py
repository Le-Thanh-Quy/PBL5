from logging import exception
from mimetypes import init
from threading import Thread
from tkinter import E, EXCEPTION
from firebase_admin import db
import firebase_admin
from firebase_admin import credentials
import time


class myThread(Thread):
    def __init__(self, serial):
        super(myThread, self).__init__()
        self.serial = serial

    def run(self):
        while True:
            res = db.reference(
                "/").child("Safes").child(self.serial).child("isOpen").get()
            if res == "True":
                print(self.serial + "Open")


def listener(event):
    print(event.event_type)
    print(event.path)
    print(event.data)  # new data at /reference/event.path. None if deleted

try:
    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://pi3b-162b7-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })
    # thread1 = myThread("123123")
    # thread1.start()
    # thread2 = myThread("11")
    # thread2.start()
    db.reference("/Safes/").child("1232153412763").listen(listener)

except Exception as ex:
    print("Error" , ex)
