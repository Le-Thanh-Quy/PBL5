import os
import re
import cv2
import face_recognition
import time
from recognition import DEF, trainingFace

def lcd_print(content, delay):
    time.sleep(delay)
    print(content)

def start_recognize_and_training(SERIAL):
    path_default = "C:\\Users\\ADMIN\\Desktop\\DoAN\\Code\\PBL5\\recognition\\DuLieuKhuonMat\\"
    ten = SERIAL
    cap = cv2.VideoCapture(0)
    soluong = 25
    sl = 0
    while sl < soluong:
        lcd_print("Training..." + str(int(sl/soluong * 100)) + "%", 0)
        ret, frame = cap.read()
        grayPic = cv2.resize(frame, (0, 0), None, fx = 0.5, fy = 0.5)
        grayPic = cv2.cvtColor(grayPic, cv2.COLOR_BGR2GRAY)
        
        faces = face_recognition.face_locations(grayPic) 
        
        for y1, x2, y2, x1 in faces:
            if not os.path.exists(f'{path_default}{ten}'):
                os.mkdir(f'{path_default}{ten}')
            cv2.imwrite(f'{path_default}{ten}\\pic{sl}.png', frame)
            sl += 1
            color = (255, 0, 0)
            stroke = 5
            cv2.rectangle(frame, (x1*2, y1*2), (x2*2, y2*2), color, stroke)
            framePos = frame[y1*2:y2*2, x1*2:x2*2]
            
        content = f'{sl}/{soluong}'    
        cv2.putText(frame, content, (16, 16), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        key = cv2.waitKey(250) # độ trễ 250/1000s
        if key == 27:  # bấm esc để thoát
            break

    cap.release()  # giải phóng camera
    cv2.destroyAllWindows()  # thoát tất cả các cửa sổ
    return trainingFace.training()