import cv2
import numpy as np

print("Package Imported")
kernel = np.ones((5, 5), np.uint8)

img = cv2.imread("./ImageRecognition/table_tennis.png")
print(img.shape)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #灰度
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0) #模糊
imgCanny = cv2.Canny(img , 100, 100) #線條偵測
imgDialation = cv2.dilate(imgCanny, kernel, iterations = 1) #線條增粗

imgResize = cv2.resize(img, (500, 500)) #更改大小
imgCropped = img[0:150, 0:150] #裁減圖片
print(imgResize.shape)

cv2.imshow("Output", img)
cv2.imshow("Gray image", imgGray)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dialation image", imgDialation)
cv2.imshow("Resize image", imgResize)
cv2.imshow("Cropped image", imgCropped)
cv2.waitKey(2000) #延遲關閉時間，0代表無限延遲
