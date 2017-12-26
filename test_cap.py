import numpy as np
import cv2

cap   = cv2.VideoCapture(0)
count = 0

while 1:
    ret, img = cap.read()
    cv2.imwrite("sek/"+str(count)+".jpg", img)
    cv2.imshow('img',img)
    k = cv2.waitKey(1) & 0xff
    count = count+1
    if count == 1000:
        break    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()