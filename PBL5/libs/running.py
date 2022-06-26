from itertools import count
from threading import Thread
import time

from flask import send_file
from recognition import NhanDien
from libs import FCMManager as fcm
from firebase_admin import db
from firebase_admin import storage

isRuning = False
isStart = False


class running(Thread):
    def __init__(self, serial, phone):
        super(running, self).__init__()
        self.serial = serial
        self.image_index = 1
        self.count = 0
        self.status = None
        self.phone = phone
        self.isImage1 = False
        self.isImage2 = False
        self.isImage3 = False
        self.isImage4 = False
        self.isImage5 = False

    def run(self):
        global isRuning, isStart
        while(True):
            if isRuning and isStart:
                result = NhanDien.start_face_recognition(
                    self.serial, self.image_index)

                print(result)
                if result != None:
                    if self.status == result:
                        self.count += 1
                    else:
                        self.count = 0
                    self.image_index += 1
                    if self.image_index > 5:
                        self.image_index = 1
                else:
                    self.count = 0
                if self.count == 5:
                    self.count = 0
                    if result:
                        isRuning = False
                        fcm.sendPush("Hi", "Mịa mày đúng là mày rồi nhập mã mà mở cửa", self.phone)
                        db.reference("/Safes/").child(self.serial).child("faceVerification").set("True")
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
        global isRuning
        if self.isImage1 and self.isImage2 and self.isImage3 and self.isImage4 and self.isImage5:
            self.isImage1 = False
            self.isImage2 = False
            self.isImage3 = False
            self.isImage4 = False
            self.isImage5 = False
            db.reference("/Safes/").child(self.serial).child("faceVerification").set("Fasle")
            fcm.sendPush("Hi", "Mịa thằng chó nào đây wtf", self.phone)
            isRuning = True
        

    def sendImageWrong(self):
        time_now = round(time.time() * 1000)
        bucket = storage.bucket()
        db.reference(
                "/Safes/").child(self.serial).child("imageWrongs").child(str(time_now)).listen(self.listener_training_image_chage)
        db.reference(
                "/Safes/").child(self.serial).child("isWrong").set(time_now)
        for i in range(1,6):
            blob = bucket.blob("Face/Wrong/" + str(time_now) + 
                                "/image" + str(i) + ".JPG")
            blob.upload_from_filename("C:\\Users\\ADMIN\\Desktop\\DoAN\\Code\\PBL5\\history\\pic" + str(i) + ".png")
            blob.make_public()
            db.reference(
                "/Safes/").child(self.serial).child("imageWrongs").child(str(time_now)).child("image" + str(i)).set(blob.public_url)
