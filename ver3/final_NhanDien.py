import cv2
import DEF
import face_recognition
import pickle
name = typelog = log = ''
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizers/Train_KhuonMat.yml")

labels = {"person_name": 1}
with open("pickles/face_labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}
    
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # grayPic = cv2.resize(frame, (0, 0), None, fx = 0.5, fy = 0.5)
    grayPic = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces =  face_recognition.face_locations(grayPic) 
    for top, right, bottom, left in faces:
        # print(x, y, w, h)
        grayPos = grayPic[top:bottom, left:right]
        id, conf = recognizer.predict(grayPos)
        print(f'{conf}')
        name = labels[id]
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.imwrite(f'nd.png', grayPos)
        if conf <= 60:
            typelog = 'info'
            log = f'{name} truy cập - không hạn chế 😝😝'
            cv2.putText(frame, name, (right + 16, bottom), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        else:
            name = "Unknow"
            typelog = 'warning'
            log = 'Thằng lạ nào định cạy két này 😒😒😒 ?!!'
            cv2.putText(frame, "???", (right + 16, bottom), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 5)
        
    DEF.savePicThread(name, frame, typelog, log)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(250) # độ trễ 250/1000s
    if key == 27:  # bấm esc để thoát
        break
    
cap.release()  # giải phóng camera
cv2.destroyAllWindows()  # thoát tất cả các cửa sổ