import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Inicializar a webcam
cap = cv2.VideoCapture(0)

# Inicializar o modelo de detecção de mãos
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        # Ler o frame da webcam
        ret, frame = cap.read()
        if not ret:
            print("Erro ao capturar o frame da câmera.")
            break

        # Converter o frame para RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detectar mãos no frame
        results = hands.process(frame_rgb)

        # Desenhar as mãos no frame
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Mostrar o frame com as mãos detectadas
        cv2.imshow('MediaPipe Hands', frame)

        # Pressione 'q' para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()