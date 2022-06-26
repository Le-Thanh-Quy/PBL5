import cv2
import face_recognition
import pickle


path_default = "C:\\Users\\ADMIN\\Desktop\\DoAN\\Code\\PBL5\\"
name = typelog = log = ''
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(path_default + "recognition\\recognizers\\face-trainner.yml")

labels = {path_default + "recognition\\person_name": 1}
with open(path_default + "recognition\\pickles\\face-labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

def start_face_recognition(ten, index):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    grayPic = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces =  face_recognition.face_locations(grayPic) 
    for top, right, bottom, left in faces:
        grayPos = grayPic[top:bottom, left:right]
        grayPos = cv2.resize(grayPos, (84, 96))
        cv2.imwrite(f'{path_default}\\history\\pic{index}.png', frame)
        id, conf = recognizer.predict(grayPos)
        name = labels[id]
        cv2.imwrite(f'nd.png', grayPos)
        if conf <= 85:
            print(f'{conf}')
            if name == ten:
                return True
            else:
                return False
        else:
            return False
    cap.release()  # giải phóng camera
    cv2.destroyAllWindows()  # thoát tất cả các cửa sổ
    return None
