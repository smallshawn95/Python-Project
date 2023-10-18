import cv2
import mediapipe as mp

# mediapipe 繪圖方法
mp_drawing = mp.solutions.drawing_utils
# mediapipe 繪圖樣式
mp_drawing_styles = mp.solutions.drawing_styles
# mediapipe 偵測手掌方法
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

# mediapipe 啟用偵測手掌
with mp_hands.Hands(
    model_complexity = 0,
    # max_num_hands = 1,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5) as hands:

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        # 將 BGR 轉換成 RGB
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # 偵測手掌
        results = hands.process(img2)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                #將節點和骨架繪製到影像中
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS, mp_drawing_styles.get_default_hand_landmarks_style(), mp_drawing_styles.get_default_hand_connections_style())

        cv2.imshow("Hand", img)
        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
