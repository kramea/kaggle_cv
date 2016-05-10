import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi

from skimage import feature

import cv2


#first = plt.imread('/Users/kalaivanikubendran/Documents/Sideprojects/kalai-kaggle-code/train_sm/set175_1.jpeg')

#first = ndi.gaussian_filter(first, 4)

im = cv2.imread('/Users/kalaivanikubendran/Documents/Sideprojects/kalai-kaggle-code/train_sm/set175_1.jpeg')
#print type(im)

edges1 = feature.canny(im)
edges2 = feature.canny(im, sigma=2)
edges3 = feature.canny(im, sigma=3)

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
                                    sharex=True, sharey=True)

ax1.imshow(edges1, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('Canny filter, $\sigma=1$', fontsize=20)

ax2.imshow(edges2, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('Canny filter, $\sigma=2$', fontsize=20)

ax3.imshow(edges3, cmap=plt.cm.gray)
ax3.axis('off')
ax3.set_title('Canny filter, $\sigma=3$', fontsize=20)

fig.tight_layout()

plt.show()