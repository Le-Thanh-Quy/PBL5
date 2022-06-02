import os
import re
import cv2
import face_recognition

rg = r"[a-zA-Z][a-zA-Z1-9]*"

ten = input('Nhập vào tên của bạn không dấu: ')
while not re.fullmatch(rg, ten):
    ten = input('Nhập vào tên của bạn không dấu: ')
cap = cv2.VideoCapture(0)
soluong = 52
sl = 0

while sl < soluong:
    ret, frame = cap.read()
    grayPic = cv2.resize(frame, (0, 0), None, fx = 0.5, fy = 0.5)
    grayPic = cv2.cvtColor(grayPic, cv2.COLOR_BGR2GRAY)
    
    faces = face_recognition.face_locations(grayPic) 
    
    for y1, x2, y2, x1 in faces:
        if not os.path.exists(f'DuLieuKhuonMat/{ten}'):
            os.mkdir(f'DuLieuKhuonMat/{ten}')
        cv2.imwrite(f'DuLieuKhuonMat/{ten}/pic{sl}.png', frame)
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