from itertools import count
from threading import Thread
from lcd_print import lcd_print, lcd_clear
import time

from flask import send_file
from recognition import NhanDien
from libs import FCMManager as fcm
from firebase_admin import db
from firebase_admin import storage

isRuning = False
isStart = False
count_wrong = 0
count_true = 0
time_now = 0


class running(Thread):
    def __init__(self, serial, phone):
        super(running, self).__init__()
        self.serial = serial
        self.image_index = 1
        self.status = None
        self.phone = phone
        self.isImage1 = False
        self.isImage2 = False
        self.isImage3 = False
        self.isImage4 = False
        self.isImage5 = False

    def run(self):
        global isRuning, isStart, count_wrong, count_true
        while(True):
            if isRuning and isStart:
                result = NhanDien.start_face_recognition(
                    self.serial, self.image_index)

                print(result)
                if result != None:
                    if result:
                        lcd_print("Keep stable: " + str(5 - count_true))
                        count_true += 1
                    if self.status == result:
                        count_wrong += 1
                    else:
                        count_wrong = 0
                        count_true = 0
                        lcd_print(" ")
                    self.image_index += 1
                    if self.image_index > 5:
                        self.image_index = 1
                else:
                    count_wrong = 0
                    count_true = 0
                if count_wrong == 5:
                    count_wrong = 0
                    if result:
                        isRuning = False
                        fcm.sendPush("Hi", "Mịa mày đúng là mày rồi nhập mã mà mở cửa", self.phone)
                        db.reference("/Safes/").child(self.serial).child("faceVerification").set("True")
                        lcd_print("Verify serial...")
                        count_true = 0
                    else:
                        isRuning = False
                        self.sendImageWrong()
                self.status = result
    
    def listener_training_image_chage(self, event):
        print(event.path)
        if event.path == "/image1":
            self.isImage1 = True
            self.checkSendImageComplete()
        elif  event.path == "/image2":
            self.isImage2 = True
            self.checkSendImageComplete()
        elif  event.path == "/image3":
            self.isImage3 = True
            self.checkSendImageComplete()
        elif  event.path == "/image4":
            self.isImage4 = True
            self.checkSendImageComplete()
        elif  event.path == "/image5":
            self.isImage5 = True
            self.checkSendImageComplete()

    def checkSendImageComplete(self):
        global isRuning, time_now
        if self.isImage1 and self.isImage2 and self.isImage3 and self.isImage4 and self.isImage5:
            self.isImage1 = False
            self.isImage2 = False
            self.isImage3 = False
            self.isImage4 = False
            self.isImage5 = False
            db.reference("/Safes/").child(self.serial).child("faceVerification").set("False")
            fcm.sendPush("Hi", "Mịa thằng chó nào đây wtf", self.phone)
            db.reference("/Safes/").child(self.serial).child("isWrong").set(time_now)
            isRuning = True
        

    def sendImageWrong(self):
        global time_now
        time_now = round(time.time() * 1000)
        bucket = storage.bucket()
        db.reference(
                "/Safes/").child(self.serial).child("imageWrongs").child(str(time_now)).listen(self.listener_training_image_chage)
        for i in range(1,6):
            blob = bucket.blob("Face/Wrong/" + str(time_now) + 
                                "/image" + str(i) + ".JPG")
            blob.upload_from_filename("/home/qthv/Desktop/PBL5/history/pic" + str(i) + ".png")
            blob.make_public()
            db.reference(
                "/Safes/").child(self.serial).child("imageWrongs").child(str(time_now)).child("image" + str(i)).set(blob.public_url)
