import cv2

img = cv2.imread("klon.jpg")

#DONUSTURMEFONK(kaynak resim, donusum flagi)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)




cv2.imshow("KLON BGR",img)
cv2.imshow("KLON RGB",img_rgb)
cv2.imshow("KLON HSV",img_hsv)
cv2.imshow("KLON GRAY",img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()