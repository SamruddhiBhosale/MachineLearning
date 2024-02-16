import cv2
import numpy as np

capture = cv2.VideoCapture(0)


while True:
    ret, frame  = capture.read()
    img_gray = cv2.cvtColor(frame , cv2.COLOR_BGR2LUV)
    cv2.imshow("video window",img_gray )
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()