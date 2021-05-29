import  cv2
import numpy as np

resim=cv2.imread("resim/logo.jpg")

kernel=np.ones((5,5),np.uint8)

erosion= cv2.erode(resim,kernel,iterations=1)

dilation = cv2.dilate(erosion,kernel, iterations=1)
#dilation2 = cv2.dilate(resim,kernel,iterations=2)

opening = cv2.morphologyEx(resim,cv2.MORPH_OPEN, kernel)
closing =cv2.morphologyEx(resim,cv2.MORPH_CLOSE,kernel)

cv2.imshow("orjinal", resim)
cv2.imshow("erosio", erosion)
cv2.imshow("dilation", dilation)
#cv2.imshow("dilation2",dilation2)

cv2.imshow("opening", opening)
cv2.imshow("closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()