import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#trackbar olustur
def nothing(x):
    pass

cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 500, 500)

cv2.createTrackbar("Lower-H", "Trackbar", 0 ,100, nothing)
cv2.createTrackbar("Lower-S", "Trackbar", 0 ,255, nothing)
cv2.createTrackbar("Lower-V", "Trackbar", 0 ,255, nothing)

cv2.createTrackbar("Upper-H", "Trackbar", 0 ,100, nothing)
cv2.createTrackbar("Upper-S", "Trackbar", 0 ,100, nothing)
cv2.createTrackbar("Upper-V", "Trackbar", 0 ,100, nothing)

#kizak pozisyonu-ust deger icin
cv2.setTrackbarPos("Upper-H", "Trackbar", 100)
cv2.setTrackbarPos("Upper-S", "Trackbar", 100)
cv2.setTrackbarPos("Upper-V", "Trackbar", 100)

#kamera goruntusu ve trackbar degisimi
while True:
     ret, frame = cap.read()
     frame = cv2.flip(frame, 1)

     #RENK UZAYİ DONUSUMU
     frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

     #TRACKBARLARIN POZISYONLARINI AL
     lower_h = cv2.getTrackbarPos("Lower-H", "Trackbar")
     lower_s = cv2.getTrackbarPos("Lower-S", "Trackbar")
     lower_v = cv2.getTrackbarPos("Lower-V", "Trackbar")

     upper_h = cv2.getTrackbarPos("Upper-H", "Trackbar")
     upper_s = cv2.getTrackbarPos("Upper-S", "Trackbar")
     upper_v = cv2.getTrackbarPos("Upper-V", "Trackbar")

     #RENK DEGERLERINI DEG ICINDE TUT
     lower_color = np.array([lower_h, lower_s, lower_v])
     upper_color = np.array([upper_h, upper_s, upper_v])


     mask = cv2.inRange(frame_hsv, lower_color, upper_color)

     cv2.imshow("original", frame)
     cv2.imshow("mask",mask)

     if cv2.waitKey(20) & 0xFF == ord("q"):
         break

cap.release()
cv2.destroyAllWindows()