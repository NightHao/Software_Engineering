import cv2
import numpy as np
url="http://192.168.3.201:8080/video"
pic_url="http://192.168.3.201:8080/shot.jpg"

cap = cv2.VideoCapture(url)
while(True):
    ret, frame = cap.read()
    if frame is not None:
        cv2.imshow('frame',frame)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break
cv2.destroyAllWindows()

# please install https://play.google.com/store/apps/details?id=com.pas.webcam
# makesure all your computer and camera are in same lan