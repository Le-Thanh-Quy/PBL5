import imp
import os
import re
import time
import cv2
from recognition import DEF, trainingFace

def lcd_print(content, delay):
    time.sleep(delay)
    print(content)

def start_recognize_and_training(SERIAL):
    rg = r"[a-zA-Z][a-zA-Z1-9]*"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    face_cascade = cv2.CascadeClassifier(
    BASE_DIR + '\\cascade\\haarcascade_frontalface_alt.xml')
    ten = SERIAL
    cap = cv2.VideoCapture(0)
    soluong = 52
    sl = 0
    uri = ""
    while sl < soluong:
        lcd_print("Training..." + str(int(sl/soluong * 100)) + "%", 0)
        ret, frame = cap.read()
        grayPic = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            grayPic, scaleFactor=1.5, minNeighbors=5)
        count = 0
        for x, y, w, h in faces:
            count = count + 1
            grayPos = grayPic[y:y+h, x:x+w]
            framePos = frame[y:y+h, x:x+w]
            if not os.path.exists(BASE_DIR + f'\\DuLieuKhuonMat\\{ten}'):
                os.mkdir(BASE_DIR + f'\\DuLieuKhuonMat\\{ten}')
            ok, anh = DEF.KiemTraAnhOK(frame)
            if ok == 1:
                if count == len(faces):
                    uri =  "C:\\Users\\ADMIN\\Desktop\\DoAN\\PBL5\\recognition\\DuLieuKhuonMat\\" + str(ten) + "\\pic" + str(sl) + ".png"
                cv2.imwrite(
                    BASE_DIR + f'\\DuLieuKhuonMat\\{ten}\\pic{sl}.png', frame)
                sl += 1

            color = (255, 0, 0)
            stroke = 5
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, stroke)
            

        content = f'{sl}/{soluong}'
        cv2.putText(frame, content, (16, 16), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        key = cv2.waitKey(250)  # độ trễ 250/1000s
        if key == 27:  # bấm esc để thoát
            break
    cap.release()
    cv2.destroyAllWindows()  
    return trainingFace.training(), uri