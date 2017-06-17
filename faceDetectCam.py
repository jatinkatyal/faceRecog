#detetct face in live feed
import cv2
camCap = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
feed = cv2.VideoWriter('feed.avi',cv2.VideoWriter_fourcc(*'XVID'),25,(640,480))
ret, frame = camCap.read()
while ret:
	faceCoord = detector.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=5)
	if len(faceCoord)>0:
		for (x,y,w,h) in faceCoord:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(50,255,50),2)
	feed.write (frame)
	cv2.imshow("face_detect",frame)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		break
	ret, frame = camCap.read()
camCap.release()	
cv2.destroyAllWindows()