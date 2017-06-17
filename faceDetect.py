#face detection
import cv2, sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QTimer

#open image
path = input("Parth:")
image = cv2.imread(path)
cv2.imshow("image",image)
cv2.waitKey(0)
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faceCoord = detector.detectMultiScale(image,scaleFactor=1.3,minNeighbors=5)
print(faceCoord)
if len(faceCoord)>0:
	for (x,y,w,h) in faceCoord:
		cv2.rectangle(image,(x,y),(x+w,y+h),(50,255,50),2)
	cv2.imshow("face_detect",image)
	cv2.waitKey(0)
else:
	print("No face detected")
cv2.destroyAllWindows()