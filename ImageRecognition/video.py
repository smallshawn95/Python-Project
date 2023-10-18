import cv2

vid = cv2.VideoCapture("./ImageRecognition/viedo.mp4")

while True:
    success, img = vid.read() #success是布林值
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
