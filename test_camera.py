import cv2
from time import gmtime
countIm    = 0
prevTime   = 0
font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture('http://admin:01290129@192.168.1.120/image/jpeg.cgi')
#http://192.168.1.120/image/jpeg.cgi
#rtsp://admin:01290129@192.168.1.220:554/live1.sdp
while True:
    ret_val, img = cam.read()
    ret_val, img2 = cam2.read()

    countIm += 1
    currentTime = gmtime().tm_sec
    if prevTime != currentTime :
        fps = countIm
        countIm = 0 #
        prevTime = currentTime
    cv2.putText(img,str(fps),(0,20), font,0.8,(0,255,0),2)
    cv2.putText(img,'fps',(35,20), font,0.7,(0,255,0),2)
    cv2.imshow('my webcam', img)
    cv2.imshow('my webcam2', img2)
    if cv2.waitKey(1) == 27: 
        break  # press 'esc' for quit