
import cv2
import face_recognition
from PIL import Image,ImageDraw
import numpy as np
from time import sleep
import time
import math
import threading
class FaceCount:
    def __init__(self):
        self.unknown_count=0

    def face_distance_to_conf(self,face_distance, face_match_threshold=0.6):
        if face_distance > face_match_threshold:
            range = (1.0 - face_match_threshold)
            linear_val = (1.0 - face_distance) / (range * 2.0)
            return linear_val
        else:
            range = face_match_threshold
            linear_val = 1.0 - (face_distance / (range * 2.0))
            return linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))

    
        


    def countUnknown(self):
        cap = cv2.VideoCapture('video3.mp4')
        facelist=[]
        while(cap.isOpened()):
            try:
                #istart=time.time()
                ret, frame = cap.read()
                #print('frame reading time------->',time.time()-istart)
                
                #start=time.time()
                rgb_frame = frame[:, :, ::-1]
                face_locations = face_recognition.face_locations(rgb_frame)
                face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
                #print("detection time----------->",time.time()-start)
                
                #start=time.time()
                cv2.imshow('frame', frame)
                for (top, right, bottom, left) in face_locations:
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.imshow('frame', frame)
                #print("showing the detected frame time----------->",time.time()-start)
                
                start=time.time()
                if facelist:     
                    for new_face_encodings in face_encodings:
                        for old_face_encodings in facelist:
                            dup=False
                            match=face_recognition.face_distance(old_face_encodings,new_face_encodings)
                            
                            for match in match:
                                if match:
                                    dup=True
                                    break
                        if not dup:
                            self.unknown_count+=1
                            facelist.append(face_encodings)
                            print("unknown people--------->",self.unknown_count)
                            #facelist.clear() 
                    
                else:
                    if face_locations:
                        print(face_locations)
                        self.unknown_count+=len(face_locations)
                        print("unknown people--------->",self.unknown_count)
                        facelist.append(face_encodings)
                #print("whole thing time----->",time.time()-istart)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            except Exception as e:
                print(e)
    # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()


if __name__=='__main__':
    t1=threading.Thread(target=FaceCount().countUnknown)
    t1.start()
    