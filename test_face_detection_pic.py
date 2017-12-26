import cv2
import numpy as np
import matplotlib.pyplot as plt

minCascade      = 1.02
maxCascade      = 5
name 			= 1
i 				= 0
offset          = 50
img 			= cv2.imread('test.jpg')
face_cascade    = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml') #frontalface_default
font = cv2.FONT_HERSHEY_SIMPLEX

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)

blur = cv2.GaussianBlur(gray,(3,3),0)
cv2.imshow('blur',blur)

laplacian = cv2.Laplacian(blur,cv2.CV_64F)
sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)
edges = cv2.Canny(img,100,400)

cv2.imshow('edge',edges)



faces = face_cascade.detectMultiScale(blur, minCascade, maxCascade) #1.3 5
for (x,y,w,h) in faces:
	cv2.imwrite("capture/face-"+str(name)+'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
	i+=1
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	cv2.putText(img,'face',(x-3,y-3), font, w*h/60000,(255,0,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()