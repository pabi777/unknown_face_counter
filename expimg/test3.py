import cv2
import face_recognition
input_movie = cv2.VideoCapture("janala.mp4")
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
# image = face_recognition.load_image_file("rupam.jpg")
# face_encoding = face_recognition.face_encodings(image)[0]
# print(face_encoding)


# Initialize variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0
unknown_count= 0

for i in range(0,length+1):
    ret, frame = input_movie.read()
    frame_number += 1
    if not ret:
        break
    rgb_frame = frame[:, :, ::-1]
    
    face_locations0 = face_recognition.face_locations(rgb_frame)
    face_encodings0 = face_recognition.face_encodings(rgb_frame, face_locations)
    known_faces = [
    face_encodings0,
    ]

    while True:
        # Grab a single frame of video
        ret, frame = input_movie.read()
        
        # Quit when the input video file ends
        if not ret:
            break

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            try:
                #print(face_encoding)
                match = face_recognition.compare_faces(known_faces, face_encoding)#tolerance=0.50)
                print(match)
            except Exception as e:
                print(e)
                continue

            name = None
            if match[0]:
                name = "Known"
            else:
                name= "Unknown"
                unknown_count+=1
            print(unknown_count)
            face_names.append(name)

        # Label the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            if not name:
                continue

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # Write the resulting image to the output video file
        #filename="frame{}-{}.jpg".format(frame_number, length))
        #cv2.imwrite(filename,frame)

# All done!
input_movie.release()
cv2.destroyAllWindows()