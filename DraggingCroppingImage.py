import numpy as np
import cv2

# img = np.zeros((512, 512, 3))
img = cv2.imread("tower.png")

flag = False
ix = -1
iy = -1

def crop(event, x, y, flags, params):
    global flag , ix, iy
    if(event == 1):
        flag = True
        ix = x
        iy = y
    elif(event == 4):
        fx = x
        fy = y
        flag = False
        cv2.rectangle(img , pt1= (ix, iy), pt2= (x,y), color= (0,0,0), thickness = 1)
        crop = img[iy : fy, ix : fx]
        cv2.imshow("new window", crop )
        cv2.waitKey(0)


cv2.namedWindow(winname = "window")
cv2.setMouseCallback("window", crop)

while True:
    cv2.imshow("window", img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()