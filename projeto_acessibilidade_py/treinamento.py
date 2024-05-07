import cv2

# Configuração da câmera
camera = cv2.VideoCapture(0)  # 0 indica a webcam padrão
largura, altura = 224, 224  # Tamanho da imagem (ajuste conforme necessário)

# Loop de captura de vídeo
while True:
    # Captura de vídeo do feed da câmera
    ret, frame = camera.read()
    if not ret:
        break
    
    # Pré-processamento do frame
    resized_frame = cv2.resize(frame, (largura, altura))
    
    # Exibição do frame
    cv2.imshow('Captura de Gestos', resized_frame)
    
    # Verificação de tecla pressionada (para sair do loop)
    key = cv2.waitKey(1)
    if key == 27:  # Pressione ESC para sair
        break

# Libera a câmera e fecha todas as janelas abertas
camera.release()
cv2.destroyAllWindows()