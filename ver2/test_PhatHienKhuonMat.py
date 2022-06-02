import numpy as np
import  cv2

face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)
i = 0
while True:
    ret, frame = cap.read()
    grayPic = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayPic, scaleFactor = 1.5, minNeighbors = 5)
    for x, y, w, h in faces:
        print(x, y, w, h)
        grayPos = grayPic[y:y+h, x:x+w]
        framePos = frame[y:y+h, x:x+w]
        cv2.imwrite(f'DuLieuKhuonMat/Vu/pic{i}.png', frame)
        i+=1
        
        color = (255, 0, 0)
        stroke = 5
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, stroke)
        
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) # độ trễ 1/1000s
    if key == 27:  # bấm esc để thoát
        break
    
cap.release()  # giải phóng camera
cv2.destroyAllWindows()  # thoát tất cả các cửa sổ