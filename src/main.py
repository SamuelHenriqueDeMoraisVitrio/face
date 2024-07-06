
import cv2
import os
import time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicialize a captura de vídeo da câmera (0 é o índice padrão para a câmera integrada)
cap = cv2.VideoCapture(0)

# Verifique se a câmera foi aberta com sucesso
if not cap.isOpened():
    print("Erro: Não foi possível abrir a câmera.")
    exit()

face_id = 0
last_capture_time = time.time()  # Tempo da última captura

while True:
    # Capture frame a frame
    ret, frame = cap.read()

    # Verifique se o frame foi lido corretamente
    if not ret:
        print("Erro: Não foi possível ler o frame.")
        break

    # Inverte horizontalmente o frame
    frame = cv2.flip(frame, 1)

    # Converta o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecte rostos no frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenhe retângulos ao redor dos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        
        # Recorte a região do rosto
        face_roi = frame[y:y+h, x:x+w]

        current_time = time.time()
        print(current_time)
        if current_time - last_capture_time >= 1:
            # Salve a imagem do rosto
            face_id += 1
            file_path = os.path.join('imgs', f'face_{face_id}.jpg')
            cv2.imwrite(file_path, face_roi)
            print(f'Rosto salvo como {file_path}')

    # Exiba o frame
    cv2.imshow('Camera', frame)

    # Quebre o loop quando a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere a captura e feche as janelas
cap.release()
cv2.destroyAllWindows()

