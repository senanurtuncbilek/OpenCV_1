import cv2
import numpy as np

img = cv2.imread("klon.jpg", 0)

row, col = img.shape

M = np.float32([[1, 0, 10],[0 ,1, 70]]) #donusum matrisi

dst = cv2.warpAffine(img, M, (row, col)) #fonk(resim adi, matris,satir,sütun)


cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()