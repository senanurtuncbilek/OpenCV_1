import cv2
import numpy as np

img = cv2.imread("klon.jpg", 0)
kernel = np.ones((10, 10), np.uint8) #birlerden olusan matrisle resmi bozdurma(int tipinde 5e5 lik matris)

erosion = cv2.erode(img, kernel, iterations = 5)  #erozyanaugrt(resimadi, dizi, iterasyon degeri(tekrarla))
dilation = cv2.dilate(img, kernel, iterations = 5) #kalinlasarak bozunum

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) #noktali-gurultulu
#CLOSE, GRADIENT, TOPHAT, BLACKHAT

cv2.imshow("original", img)
#cv2.imshow("erosion", erosion)
#cv2.imshow("dilation", dilation)
cv2.imshow("opening", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()