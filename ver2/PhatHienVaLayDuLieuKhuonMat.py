import os
import re
import cv2
import DEF
import trainingFace

rg = r"[a-zA-Z][a-zA-Z1-9]*"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

face_cascade = cv2.CascadeClassifier(BASE_DIR + '\\cascade\\haarcascade_frontalface_alt2.xml')
ten = input('Nhập vào tên của bạn không dấu: ')
while not re.fullmatch(rg, ten):
    ten = input('Nhập vào tên của bạn không dấu: ')
cap = cv2.VideoCapture(0)
soluong = 52
sl = 0
while sl < soluong:
    ret, frame = cap.read()
    grayPic = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayPic, scaleFactor = 1.5, minNeighbors = 5)
    for x, y, w, h in faces:
        grayPos = grayPic[y:y+h, x:x+w]
        framePos = frame[y:y+h, x:x+w]
        if not os.path.exists(BASE_DIR + f'\\DuLieuKhuonMat\\{ten}'):
            os.mkdir(BASE_DIR + f'\\DuLieuKhuonMat\\{ten}')
        cv2.imwrite(BASE_DIR + f'\\DuLieuKhuonMat\\{ten}\\pic{sl}.png', frame)
        sl += 1
        
        color = (255, 0, 0)
        stroke = 5
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, stroke)
    
    
    content = f'{sl}/{soluong}'    
    cv2.putText(frame, content, (16, 16), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(250) # độ trễ 250/1000s
    if key == 27:  # bấm esc để thoát
        break
    
cap.release()  # giải phóng camera
cv2.destroyAllWindows()  # thoát tất cả các cửa sổ


istrain = input('Bạn muốn train lại (y/n): ')
while not re.fullmatch(r'y|n', istrain):
    istrain = input('Bạn muốn train lại (y/n): ')
    
if istrain == 'y':
    trainingFace.training()