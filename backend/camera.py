import cv2
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("eror:camera is off")
    exit()

print("camera is on")
print("Q for exit")

while True:
    success, frame = camera.read()
    if not success:
        print("eror")
        break
    cv2.imshow("My Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()