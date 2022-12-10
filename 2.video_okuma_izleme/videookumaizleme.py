import cv2

#video
cap = cv2.VideoCapture("antalya.mp4") #videodaki kareleri yakalar

#webcam
#cap = cv2.VideoCapture(0)


while(True):
    ret, frame = cap.read() #yakalanan kareleri tek tek okur
    #cap.read() fonk u iki deger döndürür, birincisi karelerin doğru veya yanlış okunmasına bağlı bool deger, ikincisi kareleri okur
    if ret == 0:
        break

    frame = cv2.flip(frame, -1) #koordinat

    cv2.imshow("antalya",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"): #her bir frame i 1mili sn ekranda goster ve 'q'ya basinca donguden cik
        break



cap.release() #video uzerinde yapılan islem kapatilir ki siradaki islem yapilabilsin
cv2.destroyAllWindows()
