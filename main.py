# pip install cmake
# pip install dlib
# lỗi dlib thì xem đây https://www.youtube.com/watch?v=-pZEDxDRyGQ
# pip install face_recognition
# pip install opencv-python

from unittest import result
import cv2
import face_recognition

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)


imgElon1 = face_recognition.load_image_file("pics\elonmus1.jpg")
imgElon1 = cv2.cvtColor(imgElon1, cv2.COLOR_BGR2RGB)

imgElon2 = face_recognition.load_image_file("pics\elonmus2.jpg")
imgElon2 = cv2.cvtColor(imgElon2, cv2.COLOR_BGR2RGB)

face1locs = face_recognition.face_locations(imgElon1)[0] #(y1,x2,y2,x1)
encodeElon1 = face_recognition.face_encodings(imgElon1)[0]
cv2.rectangle(imgElon1,
              (face1locs[3],face1locs[0]), (face1locs[1],face1locs[2]),
              (0, 0, 255), 2)
# cv2.imshow("Elon", cv2.resize(imgElon1, (500, 500)))
# cv2.imshow("Elon2", imgElon1)
# cv2.resizeWindow("Elon2", 500, 500)
cv2.imshow("Elon1", ResizeWithAspectRatio(imgElon1, width=500))

face2locs = face_recognition.face_locations(imgElon2)[0] #(y1,x2,y2,x1)
encodeElon2 = face_recognition.face_encodings(imgElon2)[0]
cv2.rectangle(imgElon2,
              (face2locs[3],face2locs[0]), (face2locs[1],face2locs[2]),
              (0, 0, 255), 2)
imgElon2 = ResizeWithAspectRatio(imgElon2, width=500)

result = face_recognition.compare_faces([encodeElon1], encodeElon2)
value = face_recognition.face_distance([encodeElon1], encodeElon2)
print(result, round(value[0], 2))

cv2.putText(imgElon2, f'{result}, {round((round(1-value[0], 2)) * 100)}%', (25, 25),
            cv2.FONT_ITALIC, 1, (0, 0, 255), 2)

cv2.imshow("Elon2", imgElon2)

cv2.waitKey() # chờ nút nào nhấn mới tắt :3