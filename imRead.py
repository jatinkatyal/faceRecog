import cv2

image = cv2.imread("me.png",cv2.IMREAD_GRAYSCALE)
cv2.imwrite("meGray.png",image)