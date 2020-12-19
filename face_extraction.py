import cv2
import matplotlib.pyplot as plt
import dlib
from imutils import face_utils

try:
    # creating a folder named data
    if not os.path.exists('data_mouth'):
        os.makedirs('data_mouth')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data_mouth')


list_orig = os.listdir("data")  # dir is your directory path
list_mouth = os.listdir("data_mouth")
number_files_orig = len(list_orig)
number_files_mouth = len(list_mouth)

for i in range(0, number_files_mouth):
    faces =

cascPath = "/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml"
eyePath = "/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_eye.xml"
smilePath = "/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_smile.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
eyeCascade = cv2.CascadeClassifier(eyePath)
smileCascade = cv2.CascadeClassifier(smilePath)


smile = smileCascade.detectMultiScale(
    roi_gray,
    scaleFactor=1.16,
    minNeighbors=35,
    minSize=(25, 25),
    flags=cv2.CASCADE_SCALE_IMAGE
)
for (sx, sy, sw, sh) in smile:
    cv2.rectangle(roi_color, (sh, sy), (sx+sw, sy+sh), (255, 0, 0), 2)
    cv2.putText(frame, 'Smile', (x + sx, y + sy), 1, 1, (0, 255, 0), 1)
