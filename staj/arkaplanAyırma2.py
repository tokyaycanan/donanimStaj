import cv2
import numpy as np
from matplotlib import pyplot as plt

imh_bgr=cv2.imread('resim/b.png')
img_rgb= cv2.cvtColor(imh_bgr, cv2.COLOR_BGR2RGB)

rec=(0,0,250,260)

mask= np.zeros(img_rgb.shape[:2], np.uint8)

bgdModel= np.zeros((1,65),np.float64)
fgdModel = np.zeros((1, 65), np.float64)

cv2.grabCut(img_rgb, mask, rec, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

mask_2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

image_rgd_nobg = img_rgb * mask_2[:, :, np.newaxis]

plt.imshow(image_rgd_nobg), plt.axis('off')
plt.show()