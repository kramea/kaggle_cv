import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage as ndi
from skimage import feature
from skimage import data, img_as_float
from skimage.measure import structural_similarity as ssim

img = cv2.imread('/Users/kalaivanikubendran/Documents/Sideprojects/kalai-kaggle-code/train_sm/set175_1.jpeg',0)
img2 = cv2.imread('/Users/kalaivanikubendran/Documents/Sideprojects/kalai-kaggle-code/train_sm/set175_1.jpeg',0)
#img = ndi.gaussian_filter(img, 4)
edges = cv2.Canny(img,100,200)
#edges = feature.canny(img,sigma=1)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

s = ssim(edges, img)

print s