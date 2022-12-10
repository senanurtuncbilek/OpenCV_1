import cv2
import numpy as np

def nothing(x): #bos fonk
    pass

img = np.zeros((512, 512, 3), np.uint8) #pencere olustur
cv2.namedWindow("image") #pencereyi adlandir

#trackbar olusturma fonku
#fonk(kizak adi,pencere,kizagin basl-bitis degerleri, bos fonk)
cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)

switch = "0 : OFF , 1 : ON"
cv2.createTrackbar(switch, "image", 0, 1, nothing)

while True: #degisen trackbar degerleri icin pencereyi surekli yeniler
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord ("q"):
        break
    #rgb--renk, swith aciksa trackbar calisir
    #tracbarlarin degerlerini al ve pencereye yansit
    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    s = cv2.getTrackbarPos(switch, "image")
    if s == 0:
        img[:] == [0, 0 ,0]

    if s == 1:
       img[:] = [b, g, r]

cv2.destroyAllWindows()


cv2.waitKey(0)