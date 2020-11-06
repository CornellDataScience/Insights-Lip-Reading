import face_recognition
import imageio
import os
import shutil

margin = 10
maxWidth = 0
maxHeight = 0

try:
    # creating a folder named data
    if not os.path.exists('data_mouth'):
        os.makedirs('data_mouth')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data_mouth')

for i in range(0, 137):
    image = face_recognition.load_image_file("data/frame"+str(i)+".jpg")
    face_landmarks_list = face_recognition.face_landmarks(image)

    if(len(face_landmarks_list) >= 1):
        xMin = 999999
        xMax = -999999
        yMin = 999999
        yMax = -999999

        points = face_landmarks_list[0]['bottom_lip'] + \
            face_landmarks_list[0]['top_lip']

        for point in points:
            if point[0] < xMin:
                xMin = point[0]
            if point[0] > xMax:
                xMax = point[0]
            if point[1] < yMin:
                yMin = point[1]
            if point[1] > yMax:
                yMax = point[1]

        if(yMax-yMin > maxHeight):
            maxHeight = yMax-yMin

        if(xMax-xMin > maxWidth):
            maxWidth = xMax-xMin

        arr = imageio.imread("data/frame"+str(i)+".jpg")
        imageio.imsave("data_mouth/frame" + str(i) + "mouth" + ".jpg",
                       arr[yMin-margin:yMax+margin, xMin-margin:xMax+margin])
        print("FINISHED IMAGE. Maximum dimensions are " +
              str(maxWidth)+" x "+str(maxHeight))

list_orig = os.listdir("data")  # dir is your directory path
list_mouth = os.listdir("data_mouth")
number_files_orig = len(list_orig)
number_files_mouth = len(list_mouth)
if(number_files_mouth != number_files_orig):
    shutil.rmtree("data")
    print("deleted")
