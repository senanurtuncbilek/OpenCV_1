import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

fileName = "E:\webcam.avi"
codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2') #kod cozucu
frameRate = 30
resulition = (640, 480)

videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resulition) #framleri tek tek degiskene gonderir ve dosya halinde kaydeder
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) #framelerin yonunu degistirir, ayna gorunumu vb elde edebilmek, koordinatlarda oynayabilmek icin
    videoFileOutput.write(frame) #frameleri dosyaya kaydeder

    cv2.imshow("webcam live",frame)

    if(cv2.waitKey(1) & 0xFF == ord("q")):
        break
videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()
