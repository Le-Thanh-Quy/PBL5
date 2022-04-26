# pip install cmake
# pip install dlib
# lỗi dlib thì xem đây https://www.youtube.com/watch?v=-pZEDxDRyGQ
# pip install face_recognition
# pip install opencv-python

import cv2
import face_recognition
import DEF
import pandas as pd
import json
import numpy as np

df = pd.read_excel('CSDL.xlsx')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

encodes = []
for i in range(len(df.index)):
    # for j in range(1, len(df.columns)):
    for j in range(1, 2):
        data = json.loads(df.loc[i].iat[j])
        enc = np.asarray(data["value"])
        encodes.append(enc)

while True:
    ret, frame= cap.read()
    framS = cv2.resize(frame,(0,0),None,fx=0.5,fy=0.5)
    framS = cv2.cvtColor(framS, cv2.COLOR_BGR2RGB)

    # xác định vị trí khuôn mặt trên cam và encode hình ảnh trên cam
    facecurFrame = face_recognition.face_locations(framS) # lấy từng khuôn mặt và vị trí khuôn mặt hiện tại
    encodecurFrame = face_recognition.face_encodings(framS)

    for encodeFace, faceLoc in zip(encodecurFrame,facecurFrame): # lấy từng khuôn mặt và vị trí khuôn mặt hiện tại theo cặp
        # matches = face_recognition.compare_faces(df,encodeFace)
        
        faceDis = face_recognition.face_distance(encodes, encodeFace)
        print([f'{round((round((1 - x), 4) * 100),2)}%' for x in faceDis])
    
        matchIndex = np.argmin(faceDis) #đẩy về index của faceDis nhỏ nhất


        if faceDis[matchIndex] < 0.50 :
            name = df.loc[matchIndex].iat[0]
        else:
            name = "Unknow"

        #print tên lên frame
        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1*2, x2*2, y2*2, x1*2
        cv2.rectangle(frame,(x1,y1), (x2,y2),(0,255,0),2)
        cv2.putText(frame,name,(x2,y2),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)


    cv2.imshow('abc', frame)
    
    key = cv2.waitKey(1) # độ trễ 1/1000s
    if key == 27:  # bấm esc để thoát
        break
    
cap.release()  # giải phóng camera
cv2.destroyAllWindows()  # thoát tất cả các cửa sổ