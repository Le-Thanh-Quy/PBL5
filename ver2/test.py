import os
import numpy as np
from PIL import Image
import cv2
import pickle

face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

image_dir = os.path.join(BASE_DIR, 'DuLieuKhuonMat')
label_ID = {}
cur_ID = 0
x_train = []
y_label = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith('png') or file.endswith('jpg'):
            path = os.path.join(root, file)
            label = os.path.basename(os.path.dirname(path)) # lấy thư mục cha == tên
            print(label, path)
            if label in label_ID:
                pass
            else:
                label_ID[label] = cur_ID
                cur_ID += 1
            
            id_ = label_ID[label]
            print(label_ID)
            # x_train.append(path)
            # y_label.append(label)
            pil_img = Image.open(path).convert('L') # "L" mode maps to black and white pixels (and in between). "P" mode maps with a color palette.
            
            img_arr = np.array(pil_img, 'uint8')
            print(img_arr)
            faces = face_cascade.detectMultiScale(img_arr, scaleFactor = 1.5, minNeighbors = 5)
            
            for x, y, w, h in faces:
                grayPos = faces[y:y+h, x:x+w]
                x_train.append(grayPos)
                y_label.append(id_)
                
# print(y_label)
# print(x_train)

with open("label.pickle", 'wb') as f:
    pickle.dump(label_ID, f)
    
recognizer.train(x_train, np.array(y_label))
recognizer.save('training.yml')