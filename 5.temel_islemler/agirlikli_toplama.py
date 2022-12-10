#f(x,y) = x*a + y*b + c(a yogunluklu x degerine ve b yogunluklu y degeri eklenmesi sonucu yeni yogunluklu cikti elde edilir)

import cv2
import numpy as np
#olusturulan 'ayni boyuttaki' resimleri toplama

circle = np.zeros((512,512,3), np.uint8) + 255 #bos tuval
cv2.circle(circle, (256, 256), 60, (255, 0 , 0) ,-1)

rectangle = np.zeros((512,512,3), np.uint8) + 255
cv2.rectangle(rectangle, (150, 150), (350, 350),(0, 0, 255), -1)

dst = cv2.addWeighted(circle, 0.7, rectangle, 0.3, 0)
#fonk(ilk resim, yogunluk1, ikinci resim, yogunluk2, sbt sayi)

cv2.imshow("circle", circle)
cv2.imshow("rectangle", rectangle)
cv2.imshow("DST",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()