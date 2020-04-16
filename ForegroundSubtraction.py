import cv2
import numpy as np

c = cv2.VideoCapture("output.mp4")
_, f = c.read()
avg1 = np.float32(f)

while (1):

    _, f = c.read()

    cv2.accumulateWeighted(f, avg1, 0.01)

    res1 = cv2.convertScaleAbs(avg1)
    print(res1)

    cv2.imshow('img', f)
    cv2.imshow('avg1', res1)

    k = cv2.waitKey(20)

    if k == 27:
        break

cv2.destroyAllWindows()
c.release()
