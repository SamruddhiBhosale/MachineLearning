import cv2
import numpy as np





cv2.imshow("samrudhi", img)
cv2.waitKey(0)

cv2.destroyAllWindows()





# Creating our own image and drawing shapes in it 
# img = np.zeros((512, 512, 3))

# cv2.rectangle(img , pt1 = (100, 100), pt2=(300,300), color = (0, 30, 200), thickness = 3)

# cv2.circle(img , center = (400,400), radius = 50 , thickness = 2 , color = (255, 230, 0))

# cv2.line(img , pt1 = (500, 500), pt2 = (50,50), thickness = 2 , color = (230 ,0, 235))

# cv2.putText(img , text = "My First Image", org = (50, 400), thickness = 2, fontScale = 1, 
# fontFace = cv2.FONT_ITALIC , color = (255 , 255, 255), lineType = cv2.LINE_AA)

# cv2.imwrite("myFirstImage.jpg", img)


# img = cv2.imread("tower.png")
# print(img.shape)

# # Cropping of image 
# crop_img = img[0:300 , 0:300]


# Flippling of Image
# img_flip = cv2.flip(img , -1)

# Converting to Gray scale 
# img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
# print(img_gray.shape)


# Image Resizing
# resizeImg = cv2.resize(img , (img.shape[1]//2 , img.shape[0]//2))
# print(resizeImg.shape)


# Image manipulation
# img[ : , :, 2] = 0
# img_Blue = img[ : , :, 0] = 0
# img_Green = img[:, :, 1] = 0
# img_Red = img[:, :, 2] = 0

# Stacking of Images
# new_img = np.hstack((img_Blue , img_Green, img_Red))


