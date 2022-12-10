import cv2
import numpy as np
import matplotlib.pyplot as plt
#GRAFIKLESTIRME

img = cv2.imread("klon.jpg")
b, g, r = cv2.split(img) #bgr degerleri ayir

"""img = np.zeros((500, 500), np.uint8) + 50 #500e500 siyah ekran --> 500 satir ve 500 sutunluk 0 matrisi
cv2.rectangle(img, (0, 60), (200, 150), (255, 255, 255), -1)
cv2.rectangle(img, (250, 170), (350, 200), (255, 255, 255), -1)
"""
cv2.imshow("img", img)
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256]) #fonk(ravelfonk, kacdeger, aralik )
plt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()