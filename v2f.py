# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2
import face_recognition
from PIL import Image
import numpy as np


cap = cv2.VideoCapture('lp.mp4')

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
framelist=[]
while(cap.isOpened()):
	# Capture frame-by-frame
	ret, frame = cap.read()
	framelist.append(frame)
	
	for frame in framelist:
		ret2, frame2 = cap.read()
		results = face_recognition.compare_faces(frame[0],frame2[0])
		#print(results)
		if results not in framelist:
			framelist.append(frame)
		#print(len(framelist))
		# Our operations on the frame come here
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Detect faces in the image
		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(30, 30)
			#flags = cv2.CV_HAAR_SCALE_IMAGE
		)
		
		#print("Found {0} faces!".format(len(faces)))

		#Draw a rectangle around the faces
		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


		# Display the resulting frame
		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
