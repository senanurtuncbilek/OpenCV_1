import cv2
cv2.namedWindow("Klon",cv2.WINDOW_NORMAL)#pencere olusturuldu ve resim pencerenin icine yerlestirildi
#WİNDOW_NORMAL flag degeri ile pencerenin boyutlandirilabilmesi saglandi

img = cv2.imread("klon.jpg") #resmi okudu

img = cv2.resize(img,(1000,750)) #resim gormek istenilen sekilde boyutlandirildi

cv2.imshow("Klon",img) #resmi gösterdi
cv2.waitKey(0)
cv2.destroyAllWindows()