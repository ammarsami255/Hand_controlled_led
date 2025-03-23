import pickle
import cv2
import mediapipe as mp
import numpy as np
import serial
import time

arduino = serial.Serial('COM10', 9600, timeout=1)  
time.sleep(2)  

model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=False, min_detection_confidence=0.3, min_tracking_confidence=0.3)

binary_dict = {
    0: "000",
    1: "001",
    2: "010",
    3: "011",
    4: "100",
    5: "111"
}

while True:
    data_aux = []
    x_ = []
    y_ = []

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    H, W, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

        for hand_landmarks in results.multi_hand_landmarks:
            temp_data = []
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                x_.append(x)
                y_.append(y)

            min_x, min_y = min(x_), min(y_)
            
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                temp_data.append(x - min_x)
                temp_data.append(y - min_y)

            if len(temp_data) == 42:
                data_aux = temp_data

        if len(data_aux) == 42:
            prediction = model.predict([np.asarray(data_aux)])
            predicted_binary = binary_dict[int(prediction[0])]

            # إرسال التوقع إلى الأردوينو
            arduino.write(predicted_binary.encode())  
            time.sleep(0.05)  # تأخير بسيط لتجنب تداخل البيانات

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
