import cv2


def my_drawing(event, x, y, flags, params):

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 20, color=(0,0,255), thickness=10)

    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 20, color=(255,0,0), thickness=10)


cv2.namedWindow("my_img")
cv2.setMouseCallback("my_img", my_drawing)


img = cv2.imread("../imgs/dog_backpack.jpg")

while True:

    cv2.imshow("my_img", img)

    if cv2.waitKey(10) & 0xff==27:
        break

cv2.destroyAllWindows()
