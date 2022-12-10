#roi -> region of interest ---> resimdeki ilgi alani
import cv2

img = cv2.imread("klon.jpg")
print(img.shape[:2])

roi = img[30:200, 200:400] #istenilen alan(y,x)


cv2.imshow("klon", img)
cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()




