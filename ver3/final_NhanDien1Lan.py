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

def NhanDien1Lan(ten):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    grayPic = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces =  face_recognition.face_locations(grayPic) 
    for top, right, bottom, left in faces:
        # print(x, y, w, h)
        grayPos = grayPic[top:bottom, left:right]
        grayPos = cv2.resize(grayPos, (84, 96))
        id, conf = recognizer.predict(grayPos)
        # print(f'{conf}')
        name = labels[id]
        cv2.imwrite(f'nd.png', grayPos)
        if conf <= 100:
            if name == ten:
                return True
            else:
                return False
        else:
            return False
    cap.release()  # giải phóng camera
    cv2.destroyAllWindows()  # thoát tất cả các cửa sổ
    return None

# abc = NhanDien1Lan('ab123')
# print(f'{abc}')