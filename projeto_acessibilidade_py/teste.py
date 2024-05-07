import cv2

# Configuração da câmera
camera = cv2.VideoCapture(0)  # 0 indica a webcam padrão

# Loop de captura de vídeo
while True:
    # Captura de vídeo do feed da câmera
    ret, frame = camera.read()
    if not ret:
        break
    
    # Exibição do frame
    cv2.imshow('Feed de Vídeo', frame)
    
    # Verificação de tecla pressionada (para sair do loop)
    key = cv2.waitKey(1)
    if key == 27:  # Pressione ESC para sair
        break

# Libera a câmera e fecha todas as janelas abertas
camera.release()
cv2.destroyAllWindows()