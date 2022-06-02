import cv2
import threading
import os
from datetime import datetime
from PIL import Image
import pyrebase
import logging
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
face_cascade = cv2.CascadeClassifier(BASE_DIR + '\\cascade\\haarcascade_frontalface_alt.xml')
config = {
    "apiKey": "AIzaSyCyArj4NRLaeQqVzgZZ07BGKyc90xpN6z0",
    "authDomain": "test-3107.firebaseapp.com",
    "databaseURL": "https://test-3107-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "test-3107",
    "storageBucket": "test-3107.appspot.com",
    "messagingSenderId": "63571418677",
    "appId": "1:63571418677:web:6f2b978844fd49edbd5b7c"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

logging.basicConfig(filename='history.log', encoding='utf-8', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def savePic(name, pic, typelog, log):
    daynow = datetime.now().strftime("%Y_%m_%d")
    timenow = datetime.now().strftime("%H_%M_")
    if os.path.exists(BASE_DIR + f'\\Captures\\{daynow}') == False:
        os.mkdir(BASE_DIR + f'\\Captures\\{daynow}')
    npath = BASE_DIR + f'\\Captures\\{daynow}\\{timenow + name}.jpg'
    if os.path.exists(npath) == False:
        cv2.imwrite(npath, pic)
        storage.child(f'Captures/{daynow}/{timenow + name}.jpg').put(npath)
        if typelog == 'info':
            logging.info(log)
        elif typelog == 'warning':
            logging.warning(log)
    
def savePicThread(name, pic, typelog, log):
    thr1 = threading.Thread(target=savePic, args=(name, pic, typelog, log,))
    thr1.start()
    
def KiemTraAnhOK(anh):
    grayPic = cv2.cvtColor(anh, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayPic, scaleFactor = 1.5, minNeighbors = 5)
    print(len(faces))
    return len(faces), anh