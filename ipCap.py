import numpy as np
import cv2

cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture("http://admin:01290129@192.168.1.120/VIDEO.CGI")
cap2 = cv2.VideoCapture("http://admin:01290129@192.168.1.121/VIDEO.CGI")
cap3 = cv2.VideoCapture("http://admin:01290129@192.168.1.123/VIDEO.CGI")

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out0 = cv2.VideoWriter('output0.avi',fourcc, 10.0, (1280,720))
out1 = cv2.VideoWriter('output1.avi',fourcc, 10.0, (1280,720))
out2 = cv2.VideoWriter('output2.avi',fourcc, 10.0, (1280,720))
out3 = cv2.VideoWriter('output3.avi',fourcc, 10.0, (1280,720))

while(True):
    ret, frame0 = cap0.read()
    ret, frame1 = cap1.read()
    ret, frame2 = cap2.read()
    ret, frame3 = cap3.read()
    if ret==True:

        out0.write(frame0)
        out1.write(frame1)
        out2.write(frame2)
        out3.write(frame3)

        cv2.imshow("test",frame0)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap0.release()
cap1.release()
cap2.release()
cap3.release()

out0.release()
out1.release()
out2.release()
out3.release()

cv2.destroyAllWindows()
