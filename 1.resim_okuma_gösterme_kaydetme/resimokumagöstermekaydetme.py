import cv2

img = cv2.imread("klon1.jpg") #resim okuma fonksiyonu    ----fonk("isim,farklı konumdaysa konumu+ismi",tutuldugu değisken)
#print(img)

cv2.namedWindow("image",cv2.WINDOW_NORMAL) #pencereyi boyutlandirabilmek icin
cv2.imshow("image",img) #resmi gösterme
cv2.imwrite("C:\klon1.jpg",img) #resmi kaydetme
cv2.waitKey(0) #resmi ekranda tutma suresini belirler,
# 0 degeri herhangi bir tusa basmadikca veya sekmeyi kapatmadikca ekranda kalmasini saglar
cv2.destroyAllWindows() #tum penceleri iceren islemler için,her koda yazilir



