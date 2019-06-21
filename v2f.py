
import cv2
import face_recognition
from PIL import Image,ImageDraw
import numpy as np
from time import sleep
import time

cap = cv2.VideoCapture('nfs.mp4')
unknown_count=0

while(cap.isOpened()):
    start=time.time()
    try:
        # Capture frame-by-frame
        ret, frame = cap.read()
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        if face_encodings is not None:
            ret1, frame1 = cap.read()
            rgb_frame1 = frame1[:, :, ::-1]
            face_locations1 = face_recognition.face_locations(rgb_frame1)
            face_encodings1 = face_recognition.face_encodings(rgb_frame1, face_locations1)
            #print(face_encodings,face_encodings1)
            
            if face_encodings1 is not None:
                match = face_recognition.compare_faces(face_encodings, face_encodings1[0])
                for match in match:
                    if not match:
                        print(face_locations,face_locations1)
                        for (top, right, bottom, left) in face_locations:
                            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                            cv2.imshow('frame', frame)
                            unknown_count+=1
                            print(unknown_count)
                            print(time.time()-start)
            else:
                continue
        else:
            continue
        
        
        
        #print("Found {} faces! {}".format(len(face),match))

        #Draw a rectangle around the faces
        
            

        # Display the resulting frame
        #cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception as e:
       pass
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
