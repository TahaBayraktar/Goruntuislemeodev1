import cv2;
import numpy as np;

cam = cv2.VideoCapture(0)


while (True):
    ret, goruntu = cam.read()
    hsv = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)
    alt = np.array([0, 126, 20])
    ust = np.array([2, 210, 253])
    sb = cv2.inRange(hsv, alt, ust)
    renk = cv2.bitwise_and(goruntu, goruntu, mask=sb)
    cv2.imshow("Video",sb)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
