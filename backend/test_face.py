import cv2
import face_recognition

print("OpenCV:", cv2.__version__)
print("Face Recognition: OK")

image = face_recognition.load_image_file("test.jpg")

faces = face_recognition.face_locations(image)

print("Number of faces:", len(faces))