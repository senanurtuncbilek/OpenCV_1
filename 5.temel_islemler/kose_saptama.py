import cv2
import numpy as np

img = cv2.imread("15.1 text.png")
img1 = cv2.imread("15.2 contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10) #fonk(gray, max kose sayisi, kalite degeri, koseler arasi min uzaklik)
corners = np.int0(corners)

for corner in corners: #cornersin icindeki degerleri ceker
    x, y = corner.ravel() #cemberin merkez degerlerini tek bir satira doker
    cv2.circle(img, (x,y), (0 ,0 ,255), -1) #cemberi olustur

cv2.imshow("corner", img)
cv2.waitKey(0)
cv2.destroyAllWindos()