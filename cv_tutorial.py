import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.data import camera
from skimage.filters import roberts, sobel, scharr, prewitt

img = cv2.imread('/Users/kalaivanikubendran/Documents/Sideprojects/kalai-kaggle-code/train_sm/set10_1.jpeg',0)
img2 = cv2.imread('/Users/kalaivanikubendran/Documents/Sideprojects/kalai-kaggle-code/train_sm/set10_2.jpeg',0)


edges = cv2.Canny(img, 50, 100)

img3 = cv2.NORM_L2(img, img2)
print img3

#cv2.imshow('image', img3)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

#plt.show()

#edge_sobel = sobel(img)
#edge_sobel2 = sobel(img2)

#plt.imshow(edge_sobel, cmap=plt.cm.gray)
#plt.show()

#plt.imshow(edge_sobel2, cmap=plt.cm.gray)
#plt.show()

#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()

#hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
#hist, xbins, ybins = np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])

#plt.imshow(hist,interpolation = 'nearest')
#plt.show()

#surf = cv2.SURF(600)



#surf.hessianThreshold = 1000


#kp, des = surf.detectAndCompute(img, None)
#kp2, des2 = surf.detectAndCompute(img2, None)

#print len(kp)

#print des

#surf1 = cv2.drawKeypoints(img, kp, None, (255,0,0),4)

#plt.imshow(surf1), plt.show()

#surf2 = cv2.drawKeypoints(img2, kp2, None, (255,0,0),4)

#plt.imshow(surf2), plt.show()
