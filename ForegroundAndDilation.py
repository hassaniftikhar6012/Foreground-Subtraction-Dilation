import cv2
import numpy as np

cap = cv2.VideoCapture("output.mp4")
subtractor = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=30, detectShadows=True)

while True:
    _, first_frame = cap.read()
    mask = subtractor.apply(first_frame)

    cv2.imshow('FirstFrame', first_frame)
    cv2.imshow('mask', mask)
  #  cv2.imshow('Mean', fg)
    key = cv2.waitKey(30)
    if key == 27:
        break
cap.release()
cv2.detroyAllWindows()
