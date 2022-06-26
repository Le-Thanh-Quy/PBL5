import cv2
import os
import re
import numpy as np
from PIL import Image
import pickle
import face_recognition

recognizer = cv2.face.LBPHFaceRecognizer_create()
path_default = "C:\\Users\\ADMIN\\Desktop\\DoAN\\Code\\PBL5\\recognition\\"

def training():
    nnn = 0
    current_id = 0
    label_ids = {}
    y_labels = []
    x_train = []
    
    for root, dirs, files in os.walk(path_default + "DuLieuKhuonMat"):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                nnn += 1
                print(nnn)
                path = os.path.join(root, file)
                label = os.path.basename(root).replace(" ", "-").lower()
                if not label in label_ids:
                    label_ids[label] = current_id
                    current_id += 1
                id_ = label_ids[label]
                pil_image = Image.open(path).convert("L")
                image_array = np.array(pil_image, "uint8")
                faces = face_recognition.face_locations(image_array)
                
                for top, right, bottom, left in faces:
                    face = image_array[top:bottom, left:right]
                    face = cv2.resize(face, (84, 96))
                    try:
                        cv2.imwrite('Training.png', face)
                        x_train.append(face)
                        y_labels.append(id_)
                    except:
                        pass

    with open(path_default + "pickles\\face-labels.pickle", 'wb') as f:
        pickle.dump(label_ids, f)
    recognizer.train(x_train, np.array(y_labels))
    recognizer.save(path_default + "recognizers\\face-trainner.yml")
    return True