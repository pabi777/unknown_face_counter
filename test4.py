import face_recognition
known_image = face_recognition.load_image_file("lp/frame334.jpg")
unknown_image = face_recognition.load_image_file("lp/frame335.jpg")
print(known_image)
biden_encoding = face_recognition.face_encodings(known_image)[0]
print(biden_encoding)
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
print(results)