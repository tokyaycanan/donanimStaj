import cv2

resim = cv2.imread("resim/b.png")

mean_filter=cv2.blur(resim,(3,3))
mean_filter2=cv2.blur(resim,(5,5))
mean_filter3=cv2.blur(resim,(5,5))

median_filter=cv2.medianBlur(resim,3)
median_filter2=cv2.medianBlur(resim,5)
median_filter3=cv2.medianBlur(resim,7)


gauss= cv2.GaussianBlur(resim,(3,3),0)
gauss2=cv2.GaussianBlur(resim,(5,5),0)
gauss3= cv2.GaussianBlur(resim,(7,7),0)


cv2.imshow("orjinal goruntu", resim)
cv2.imshow("mean_filter", mean_filter)
cv2.imshow("mean_filter2", mean_filter2)
cv2.imshow("mean_filter3", mean_filter3)

cv2.imshow("median_filter",median_filter)
cv2.imshow("median_filter2",median_filter2)
cv2.imshow("median_filter3",median_filter3)

cv2.imshow("gauss",gauss)
cv2.imshow("gauss2",gauss2)
cv2.imshow("gauss3",gauss3)

cv2.waitKey(0)
cv2.destroyAllWindows()