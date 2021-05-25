from PIL import Image
from PIL import ImageFilter
from numpy import asarray
import numpy as np


img = Image.open("Car_number.jpg")

img=img.convert('L')
img = np.array(img)

for i in range(len(img)):
    for j in range(0,len(img[1])):
        if img[i][j] < 200:
            img[i][j] = 255
        else :
            img[i][j] = 0

img = Image.fromarray(img)



img1 = img.filter(ImageFilter.DETAIL)
img1 = img1.filter(ImageFilter.SHARPEN)
img1 = img1.filter(ImageFilter.EDGE_ENHANCE_MORE)


img1.save("test1.jpg")