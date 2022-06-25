import os
import cv2
import pickle
from recognition import DEF


def start_face_recognition():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    face_cascade = cv2.CascadeClassifier(
        BASE_DIR + '\\cascade\\haarcascade_frontalface_alt.xml')
    name = typelog = log = ''
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(BASE_DIR + "\\recognizers\\face-trainner.yml")

    labels = {"person_name": 1}
    with open(BASE_DIR + "\\pickles\\face-labels.pickle", 'rb') as f:
        og_labels = pickle.load(f)
        labels = {v: k for k, v in og_labels.items()}

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        grayPic = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            grayPic, scaleFactor=1.5, minNeighbors=5)
        for x, y, w, h in faces:
            # print(x, y, w, h)
            grayPos = grayPic[y:y+h, x:x+w]
            id, conf = recognizer.predict(grayPos)
            # print(f'{conf}')
            name = labels[id]
            font = cv2.FONT_HERSHEY_SIMPLEX
            if conf <= 60:
                typelog = 'info'
                log = f'{name} truy cập - không hạn chế 😝😝'
                cv2.putText(frame, name, (x+w + 16, y+h), font,
                            1, (255, 255, 255), 2, cv2.LINE_AA)
            else:
                name = "Unknow"
                typelog = 'warning'
                log = 'Thằng lạ nào định cạy két này 😒😒😒 ?!!'
                cv2.putText(frame, "???", (x+w + 16, y+h), font,
                            1, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)

        DEF.savePicThread(name, frame, typelog, log)
        cv2.imshow('frame', frame)
        key = cv2.waitKey(250)  # độ trễ 250/1000s
        if key == 27:  # bấm esc để thoát
            break

    cap.release()  # giải phóng camera
    cv2.destroyAllWindows()  # thoát tất cả các cửa sổ
