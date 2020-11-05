import face_recognition
import imageio

margin = 10
maxWidth = 0
maxHeight = 0

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
        imageio.imsave("data/frame" + str(i) + "mouth" + ".jpg",
                       arr[yMin-margin:yMax+margin, xMin-margin:xMax+margin])
        print("FINISHED IMAGE. Maximum dimensions are " +
              str(maxWidth)+" x "+str(maxHeight))
