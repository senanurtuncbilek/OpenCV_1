import cv2
import numpy as np

img = cv2.imread("klon.jpg")
dimension = img.shape
print(dimension)
#img.shape img icerinde tutulan resmin boyutlarini ve kanal verisini(renkli--3,sb--2) verir
#her piksel uc renk tutar--> kym

color = img[420, 500] #bu pikseldeki renk degerine erisir
print("BGR: ", color)

blue = img[420, 500, 0] #koordinattaki mavi degerine erisir
print("blue: ", blue)

green = img[420, 500, 1]
print("green: ", green)

red = img[420, 500, 2]
print("red: ", red)


"----------------------------------------------"
#degerleri degistirme

img[420, 500, 0] = 250
print("new blue: ", img[420, 500, 0])

blue1 = img.item(150, 200, 0)
print("blue1: ", blue1)
img.itemset((150, 200, 0), 172)
print("new blue1: ", img[150, 200, 0])




cv2.imshow("klon asker", img)
cv2.waitKey(0)
cv2.destroyAllWindows()