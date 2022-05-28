import cv2
import face_recognition
import DEF
import pandas as pd
import json
import numpy as np

linkIMGCheck = "Test3.jpg" # Test1.jpg Test2.jpg Test3.jpg
df = pd.read_excel('CSDL.xlsx')

encodes = []
for i in range(len(df.index)):
    # for j in range(1, len(df.columns)):
    for j in range(1, 2):
        data = json.loads(df.loc[i].iat[j])
        enc = np.asarray(data["value"])
        encodes.append(enc)

imgCheck = face_recognition.load_image_file(linkIMGCheck)
imgCheck = cv2.cvtColor(imgCheck,cv2.COLOR_BGR2RGB)
imgCheck = DEF.ResizeWithAspectRatio(image=imgCheck, width=800)
encodeCheck = DEF.getMaHoa(linkIMGCheck)

faceDis = face_recognition.face_distance(encodes, encodeCheck)
print([f'{round((round((1 - x), 4) * 100),2)}%' for x in faceDis])
matchIndex = np.argmin(faceDis) # lấy index khoảng cách nhỏ nhất == giống nhất
if faceDis[matchIndex] < 0.50 :
    name = df.loc[matchIndex].iat[0]
else:
    name = "Unknow"

y1, x2, y2, x1 = face_recognition.face_locations(imgCheck)[0]
cv2.rectangle(imgCheck, (x1,y1), (x2,y2), (255,0,255), 2)
cv2.putText(imgCheck, name,(x2 + 10,y2),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

cv2.imshow("Check", imgCheck)
cv2.waitKey()
cv2.destroyAllWindows()