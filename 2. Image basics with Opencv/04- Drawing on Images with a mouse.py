import cv2
import numpy as np


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 20, color=(255, 0, 0), thickness=-1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 20, color=(0,0,255), thickness=-1)


cv2.namedWindow("my_drawing")
cv2.setMouseCallback("my_drawing", draw_circle)

img = np.zeros(shape=(512, 512, 3), dtype=np.int8)

while True:

    cv2.imshow("my_drawing", img)

    if cv2.waitKey(20) & 0xff == 27:
        break

cv2.destroyAllWindows()
