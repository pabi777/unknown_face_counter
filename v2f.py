
import cv2
import face_recognition
from PIL import Image,ImageDraw
import numpy as np
from time import sleep
import time
import math

def face_distance_to_conf(face_distance, face_match_threshold=0.6):
    if face_distance > face_match_threshold:
        range = (1.0 - face_match_threshold)
        linear_val = (1.0 - face_distance) / (range * 2.0)
        return linear_val
    else:
        range = face_match_threshold
        linear_val = 1.0 - (face_distance / (range * 2.0))
        return linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))

def countUnknown():
    cap = cv2.VideoCapture('nfs.mp4')
    unknown_count=0
    d=0
    facelist=[]
    face_encodings=None
    while(cap.isOpened()):
        start=time.time()
        try:
            if len(facelist)>=10:
                facelist.clear()
            # Capture frame-by-frame
            ret, frame = cap.read()
            rgb_frame = frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.imshow('frame', frame)
            
            if face_encodings:
                facelist.append(face_encodings[0])
                if d==0:
                    print(face_encodings)
                    unknown_count=len(face_locations)
                    d+=1
                    print(unknown_count)
            
            key = cv2.waitKey(1000)
            ret1,frame1= cap.read()
            rgb_frame1 = frame1[:, :, ::-1]
            face_locations1 = face_recognition.face_locations(rgb_frame1)
            face_encodings1 = face_recognition.face_encodings(rgb_frame1, face_locations1)

            
            old_max_people=(len(face_locations))
            new_max_people=(len(face_locations1))
            print(new_max_people,old_max_people)
            if new_max_people>old_max_people:
                for f in facelist:
                    faceDistance=face_recognition.face_distance(face_encodings1,f)#face_recognition.compare_faces(face_encodings1,f)
                    #print(face_distance_to_conf(faceDistance))
                    for faced in faceDistance:
                        match=abs(face_distance_to_conf(faced))
                        print(match)
                        #for match in match:
                        if match<0.40:
                            new_people=abs(new_max_people-old_max_people)
                            unknown_count+=new_people
                            print(unknown_count)
                        
                #if face_encodings1 is not None:
                    
                    # for face_encodings in facelist:
                    #     for face1 in face_encodings1:
                    #         faceDistance = face_recognition.face_distance([face_encodings], face1)
                    #         print(faceDistance)
                            
                    #         match=face_recognition.compare_faces([face_encodings], face1)[0][0] #abs(face_distance_to_conf(faceDistance)[0])
                    #         print(match)
                    #         if not match:
                    #             unknown_count+=1
                    #             print(unknown_count)
                    #             #print(time.time()-start)
                # else:
                #     cv2.imshow('frame', frame)
                #     continue
            
            
            
            #print("Found {} faces! {}".format(len(face),match))

            #Draw a rectangle around the faces
            
                

            # Display the resulting frame
            #cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        except Exception as e:
            raise
            print(e)
# When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__=='__main__':
    countUnknown()
    