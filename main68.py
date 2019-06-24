import cv2
import numpy as np
import dlib
import math
import time
import face_recognition
#cap = cv2.VideoCapture('nfs.mp4')
distance = lambda x1,x2,y1,y2:math.sqrt((x2-x1)**2 + (y2-y1)**2)

def face_distance_to_conf(face_distance, face_match_threshold=0.6):
    if face_distance > face_match_threshold:
        range = (1.0 - face_match_threshold)
        linear_val = (1.0 - face_distance) / (range * 2.0)
        return linear_val
    else:
        range = face_match_threshold
        linear_val = 1.0 - (face_distance / (range * 2.0))
        return linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))

def linepredict(frame):
    start=time.time()
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    jawx=[]
    jawy=[]
    nosex=[]
    nosey=[]
    diffx=[]
    diffy=[]
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    landmarkslist=[]
    print(len(faces))
    for face in faces:
        #faceratio=[]
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
        landmarks=predictor(gray, face)
        landmarkslist.append(face)
        #print(landmarks)

        for n in range(0,68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 4, (255, 0, 0), -1)

    cv2.imshow("Frame", frame)
    #print(time.time()-start)
    key = cv2.waitKey(1)
    
    return (landmarkslist)


if __name__=='__main__':
    cap = cv2.VideoCapture('video3.mp4')
    count=0
    while True:
        _, frame = cap.read()
        lms=linepredict(frame)
        # ret,frame1= cap.read()
        # lms1=linepredict(frame1)
        # for lms1 in lms:
        #     score=face_recognition.face_distance(lms,lms1)
        #     print(score)

