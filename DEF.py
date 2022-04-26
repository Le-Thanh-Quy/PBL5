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

def getMaHoa(path):
    curImg = cv2.imread(path)
    curImg = cv2.cvtColor(curImg, cv2.COLOR_RGB2BGR)
    encode = face_recognition.face_encodings(curImg)[0]
    return encode