import cv2
import numpy as np

img = cv2.imread("klon.jpg")
row = img.shape[0]
col = img.shape[1]

M = cv2.getRotationMatrix2D((col/2, row/2), 90, 1) #iki boyutta yon deg--> fonk(satir, sütun, dondurme yonu,olcek)

dst = cv2.warpAffine(img, M, (col, row))

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
