import numpy as np
import cv2

img = np.zeros((512, 512, 3))


flag = False
ix = -1
iy = -1



def draw (event , x, y, flags , params) :
    global flag , ix, iy
    
    if event == 1:
        flag = True
        ix = x
        iy = y
    elif event == 0 :
        if flag == True :
            cv2.rectangle(img , pt1 = (ix, iy), pt2 = (x , y), color = (150 , 150 , 0), thickness = -1)

    elif event == 4:
        flag = False
        cv2.rectangle(img , pt1 = (ix, iy), pt2 = (x , y), color = (150 , 150 , 0), thickness = -1)

cv2.namedWindow(winname = "window")
cv2.setMouseCallback("window", draw)

while True :
    cv2.imshow("window", img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
