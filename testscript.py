import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import glob, os

print "test output"

from subprocess import check_output
#print(check_output(["ls", "../input"]).decode("utf8"))
smjpegs = [f for f in glob.glob("../train_sm/*.jpeg")]
print(smjpegs[:9])

set175 = [smj for smj in smjpegs if "set175" in smj]
print(set175)

edges2 = feature.canny(set175, sigma=3)

first = plt.imread('/Users/kalaivanikubendran/Documents/Sideprojects/kalai-kaggle-code/train_sm/set175_1.jpeg')
dims = np.shape(first)
print dims

np.min(first), np.max(first)

pixel_matrix = np.reshape(first, (dims[0] * dims[1], dims[2]))
print(np.shape(pixel_matrix))

plt.scatter(pixel_matrix[:,0], pixel_matrix[:,1])
_ = plt.hist2d(pixel_matrix[:,1], pixel_matrix[:,2], bins=(50,50))

#
# fifth = plt.imread('../input/train_sm/set175_5.jpeg')
# dims = np.shape(fifth)
# pixel_matrix5 = np.reshape(fifth, (dims[0] * dims[1], dims[2]))
#
# _ = plt.hist2d(pixel_matrix5[:,1], pixel_matrix5[:,2], bins=(50,50))
#
# _ = plt.hist2d(pixel_matrix[:,2], pixel_matrix5[:,2], bins=(50,50))

