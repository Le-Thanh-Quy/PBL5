import cv2
import os
import re
import numpy as np
from PIL import Image
import pickle
import face_recognition

recognizer = cv2.face.LBPHFaceRecognizer_create()
arr = []

def training():
    nnn = 0
    current_id = 0
    label_ids = {}
    y_labels = []
    x_trains = []
    
    for root, dirs, files in os.walk("DuLieuKhuonMat"):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root, file)
                label = os.path.basename(root).replace(" ", "-").lower()
                if not label in label_ids:
                    label_ids[label] = current_id
                    current_id += 1
                id_ = label_ids[label]
                img = cv2.imread(path)
                # rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                rgb = img
                faces = face_recognition.face_locations(rgb)
                
                for top, right, bottom, left in faces:
                    face = rgb[top:bottom, left:right]
                    encodings = face_recognition.face_encodings(rgb, faces)
                    try:
                        cv2.imwrite('Training.png', face)
                        x_trains.append(encodings[0])
                        y_labels.append(id_)
                        arr.append([id_, encodings[0]])
                        nnn += 1
                        print(f'{nnn}')
                    except:
                        pass
               
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    import pandas as pd
    
    df = pd.DataFrame(arr, columns=['id', 'encode'])
    df.to_csv('data.csv')
    
    print(y_labels)
    print(len(y_labels))
    print(len(x_trains))
    
    x_train, x_test, y_train, y_test = train_test_split(x_trains, y_labels, test_size = 0.3, random_state = 0)
    # classifier = LogisticRegression(max_iter = 1234)
    classifier = LogisticRegression()
    model = classifier.fit(x_trains, y_labels)
    print(model.score(x_trains, y_labels))
    
    
    with open("pickles/model.pickle", 'wb') as f:
        pickle.dump(model, f)
    
    # print(label_ids)
    
    # with open("pickles/face_labels.pickle", 'wb') as f:
    #     pickle.dump(label_ids, f)
    # recognizer.train(x_trains, np.array(y_labels))
    # recognizer.save("recognizers/Train_KhuonMat.yml")
    
training()