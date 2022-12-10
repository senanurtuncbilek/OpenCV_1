import cv2
import numpy as np

img = cv2.imread("3.2 h_line.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 150) #resimlerdeki koseleri tespit eder(gray, min, max)


lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap = 200) #cizgileri tespit eder, fonk(koseleri bulunmus resim,aci degerleri.., theshold deg, cizgileri tamamlayan deger)
#print(lines)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2) #cizgilerin üzerinden gecer, fonk(resim, basl-bitis deg.., renk, kalinlik)



cv2.imshow("gray", gray)
cv2.imshow("edges", edges)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()