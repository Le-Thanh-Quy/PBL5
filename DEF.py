import cv2
import face_recognition
import threading
import os
from datetime import datetime
import pyrebase
import logging

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

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

def getMaHoa(path):
    curImg = cv2.imread(path)
    curImg = cv2.cvtColor(curImg, cv2.COLOR_RGB2BGR)
    encode = face_recognition.face_encodings(curImg)[0]
    return encode

def savePic(name, pic, typelog, log):
    daynow = datetime.now().strftime("%Y_%m_%d")
    timenow = datetime.now().strftime("%H_%M_")
    if os.path.exists(f'./Captures/{daynow}') == False:
        os.mkdir(f'./Captures/{daynow}')
    npath = f'./Captures/{daynow}/{timenow + name}.jpg'
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