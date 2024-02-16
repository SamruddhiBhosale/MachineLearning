import cv2
import numpy as np

img = np.zeros((512, 512, 3))

def draw(event , x , y, flags, params) :
    if(event == 1) :
        cv2.circle(img , center = (x , y), radius = 20, color = (200 , 100 , 0), thickness = -1)


cv2.namedWindow(winname = "samrudhi")
cv2.setMouseCallback("samrudhi", draw)

while True :
    cv2.imshow("samrudhi", img)

    if cv2.waitKey(1) & 0xFF == ord('x') :
        break
cv2.destroyAllWindows()