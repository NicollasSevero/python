import cv2

# Carrega o vídeo
video_path = 'caminho_para_seu_video.mp4'
cap = cv2.VideoCapture(video_path)

# Verifica se o vídeo foi aberto corretamente
if not cap.isOpened():
    print("Erro ao abrir o vídeo")
    exit()

# Loop para ler e exibir cada quadro do vídeo
while True:
    ret, frame = cap.read()

    # Verifica se chegou ao fim do vídeo
    if not ret:
        break

    # Mostra o quadro do vídeo
    cv2.imshow('Video', frame)

    # Pressione 'q' para sair do loop
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Libera os recursos
cap.release()
cv2.destroyAllWindows()