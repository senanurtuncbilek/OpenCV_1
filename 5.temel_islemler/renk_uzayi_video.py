import cv2
#VIDEOLARDA RENK UZAYI DONUSUMU
cap = cv2.VideoCapture("antalya.mp4")

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if ret == False:
        break

    cv2.imshow("video", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
