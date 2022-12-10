import cv2
#RESMİ YENİDEN BOYUTLANDİRMA
def resizewithAspectRatio(img, width= None, height= None, inter = cv2.INTER_AREA):
   #def fonkadi (resmin tutuldugu degisken, girdigim en degeri, girdigim boy degeri, yeniden boyutlandirmalarda cakismalari onlemek icin atanan default deger):

    dimension = None #resmin yeni boyutlarini girmek icin degisken
    (h, w) = img.shape[:2] #fonknun icindeki img değiskenli resmin boyutlarini alir(tanimli boyutlari), img.shape[]--> resmin boyutlarina erisir.

    if(width is None and height is None):
        return img  #iki degerde None ise resmin default halini verir

   #bir tanesi girilmisse, girilen deger gercek degere bolunerek oran bulunur, orana gore girilmeyen deger alinir
    if(width is None):
        r = height/float(h)
        dimension = (int(w*r), height)
    else:
        r = width/float(w)
        dimension = (width,int(h*r))

    return cv2.resize(img, dimension, interpolation= inter)

img = cv2.imread("klon1.jpg")
img1 = resizewithAspectRatio(img, width= None, height = 600, inter=cv2.INTER_AREA)

cv2.imshow("original", img)
cv2.imshow("Resized",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

