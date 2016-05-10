import PIL
from PIL import Image

basewidth = 300
 img = Image.open('/Users/kalaivanikubendran/Documents/Sideprojects/kalai-kaggle-code/train_sm/set10_1.jpeg')
 wpercent = (basewidth / float(img.size[0]))
 hsize = int((float(img.size[1]) * float(wpercent)))
 img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
 img.save('10-1-sm.jpg')