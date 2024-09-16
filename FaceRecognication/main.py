import cv2

# Loading The Cascade File
haar_cascade_face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml.xml")
face_cascade = cv2.CascadeClassifier("haar_cascade_face")
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# Reading the Input Image
image = cv2.imread('1.jpg')
# image = cv2.imread('download.jfif')

# Resizing the Image
img = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Converting the image into grayscale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecting The Faces
faces = face_cascade.detectMultiScale(imgGray, 1.2, 5)


# Pointing The Faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Displaying The Output Image
cv2.imshow('img', img)
cv2.waitKey()
