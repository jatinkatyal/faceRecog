import cv2
#capture image
camCap = cv2.VideoCapture(0)
ret, frame = camCap.read()
camCap.release()
#save image
cv2.imwrite("capture.jpg",frame)
#display captured frame
cv2.imshow("capture",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

#write and display video feed
camCap = cv2.VideoCapture(0)
feed = cv2.VideoWriter('feed.avi',cv2.VideoWriter_fourcc(*'XVID'),25,(640,480))
ret, frame = camCap.read()
while ret:
	feed.write (frame)
	cv2.imshow("Video feed",frame)
	ret, frame = camCap.read()
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break
camCap.release()	
cv2.destroyAllWindows()