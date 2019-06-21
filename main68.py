import cv2
import numpy as np
import dlib
import math
import time

#cap = cv2.VideoCapture('nfs.mp4')
distance = lambda x1,x2,y1,y2:math.sqrt((x2-x1)**2 + (y2-y1)**2)

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
    for face in faces:
        #faceratio=[]
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        landmarks = predictor(gray, face)
        #print(landmarks)

        for n in range(0, 8):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            jawx.append(x)
            jawy.append(y)
            cv2.circle(frame, (x, y), 4, (255, 0, 0), -1)

        for n in range(28,36):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            nosex.append(x)
            nosey.append(y)
            cv2.circle(frame, (x, y), 4, (255, 0, 0), -1)

        

        for i in range(0,8):
            diffx.append(distance(jawx[i],nosex[i],jawy[i],nosey[i]))
            #diffy.append(abs(jawy[i]-nosey[i]))
    
    cv2.imshow("Frame", frame)
    print(time.time()-start)
    key = cv2.waitKey(1)
    
    return (diffx)
if __name__=='__main__':
    cap = cv2.VideoCapture('nfs.mp4')
    while True:
        _, frame = cap.read()
        p=linepredict(frame)
