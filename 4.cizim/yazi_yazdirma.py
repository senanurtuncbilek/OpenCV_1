import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype = np.uint8) + 255

font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

cv2.putText(canvas, "IkiNs",(100, 100), font1, 4, (0,0,0), cv2.LINE_AA) #yazi yazdirmak icin kullanilan fonk
#fonk(pencere,yazi,koordinat,font buyuklugu, renk, yazi tipi)






cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()