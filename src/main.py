
import cv2

# Inicialize a captura de vídeo da câmera (0 é o índice padrão para a câmera integrada)
cap = cv2.VideoCapture(0)

# Verifique se a câmera foi aberta com sucesso
if not cap.isOpened():
    print("Erro: Não foi possível abrir a câmera.")
    exit()

while True:
    # Capture frame a frame
    ret, frame = cap.read()

    # Verifique se o frame foi lido corretamente
    if not ret:
        print("Erro: Não foi possível ler o frame.")
        break

    # Exiba o frame
    cv2.imshow('Camera', frame)

    # Quebre o loop quando a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere a captura e feche as janelas
cap.release()
cv2.destroyAllWindows()

