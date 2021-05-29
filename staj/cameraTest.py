
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')
cv2.moveWindow('frame', 10, 10)
cv2.namedWindow('gray')
cv2.moveWindow('gray', 690, 10)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height
while (True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    k = cv2.waitKey(30) & 0xff
    if k == 27 or k == ord('q'):  # press 'ESC' or 'q' to quit
        break
cap.release()
cv2.destroyAllWindows()