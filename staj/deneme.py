import cv2
import numpy as np

# kamera başlatma
kamera = cv2.VideoCapture(0)

# belirlenen sürede görüntü tekrarı
while True:

    ret, goruntu = kamera.read()
    # goruntu uzerine belirlenen konumda belirlenen renkte ve belirlenen kalınlıkta dikdortgen çizimi
    cv2.rectangle(goruntu, (150, 150), (300, 300), (25, 20, 100), 2)
    # goruntu uzerine belirlenen konumda belirlenen renkte ve belirlenen kalınlıkta çizgi çizimi
    cv2.line(goruntu, (150, 150), (300, 300), (255, 255, 255), 3)
    # goruntu uzerine belirlenen konumda belirlenen renkte ve belirlenen kalınlıkta daire çizimi
    cv2.circle(goruntu, (300, 300), 60, (88, 102, 45), 1)
    # goruntu uzerine belirlenen konumda belirlenen renkte ve belirlenen kalınlıkta metin yazdırma
    cv2.putText(goruntu, "CANAN", (130, 140), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    cv2.imshow("deneme", goruntu)
    # çikis kontrolü
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# kamerayı serbest bırakma
kamera.release()

cv2.destroyWindow()
