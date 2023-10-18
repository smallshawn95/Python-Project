import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640) #長
cap.set(4, 480) #寬
cap.set(10, 200) #亮度

while True:
    success, img = cap.read() #success是布林值
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
