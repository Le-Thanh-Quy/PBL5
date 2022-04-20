# pip install cmake
# pip install dlib
# lỗi dlib thì xem đây https://www.youtube.com/watch?v=-pZEDxDRyGQ
# pip install face_recognition
# pip install opencv-python

import cv2
import face_recognition
import DEF

src1 = "pics\elonmus1.jpg"
src2 = "pics\elonmus2.jpg"

imgElon1 = face_recognition.load_image_file(src1)
imgElon1 = DEF.ResizeWithAspectRatio(imgElon1, width=500)
imgElon1 = cv2.cvtColor(imgElon1, cv2.COLOR_BGR2RGB)

imgElon2 = face_recognition.load_image_file(src2)
imgElon2 = DEF.ResizeWithAspectRatio(imgElon2, width=500)
imgElon2 = cv2.cvtColor(imgElon2, cv2.COLOR_BGR2RGB)

face1locs = face_recognition.face_locations(imgElon1)[0] #(y1,x2,y2,x1)
encodeElon1 = face_recognition.face_encodings(imgElon1)[0]
cv2.rectangle(imgElon1,
              (face1locs[3],face1locs[0]), (face1locs[1],face1locs[2]),
              (0, 0, 255), 2)

face2locs = face_recognition.face_locations(imgElon2)[0] #(y1,x2,y2,x1)
encodeElon2 = face_recognition.face_encodings(imgElon2)[0]
cv2.rectangle(imgElon2,
              (face2locs[3],face2locs[0]), (face2locs[1],face2locs[2]),
              (0, 0, 255), 2)

result = face_recognition.compare_faces([encodeElon1], encodeElon2)
value = face_recognition.face_distance([encodeElon1], encodeElon2)
print(result, round(value[0], 2))

cv2.putText(imgElon2, f'{result[0]}, {round((round(1-value[0], 2)) * 100)}%', (25, 25),
            cv2.FONT_ITALIC, 1, (0, 0, 255), 2)

cv2.imshow("Origin", imgElon1)
cv2.imshow("Check", imgElon2)

cv2.waitKey() # chờ nút nào nhấn mới tắt :3