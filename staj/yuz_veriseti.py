import cv2
from past.builtins import raw_input
kamera = cv2.VideoCapture(0)
kamera.set(3, 640)  # video genişliğini belirle
kamera.set(4, 480)  # video yüksekliğini belirle
face_detector = cv2.CascadeClassifier('Cascades/data/haarcascade_frontalface_default.xml')
# Her farklı kişi için farklı bir yüz tamsayısı ata
# face_id = input('\n enter user id end press <return> ==>  ')
MAXFOTOSAY = 50  # Her bir yüz için kullanılacak imaj sayısı
Id=raw_input('ID Giriniz:')
sampleNum=0
print("\n [INFO] Kayıtlar başlıyor. Kameraya bak ve bekle ...")

say = 0

while (True):
    ret, img = kamera.read()
    # img = cv2.flip(img, -1) # gerekiyorsa kullan
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    yuzler = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in yuzler:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        sampleNum = sampleNum + 1
        # Yakalanan imajı veriseti klasörüne kaydet
        cv2.imwrite("veriseti/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('YUZ TARAMA',img)
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif sampleNum > 20:
        break

# Belleği temizle
print("\n [INFO] Program sonlanıyor ve bellek temizleniyor.")
kamera.release()
cv2.destroyAllWindows()