from PIL import Image
from PIL import ImageFilter

img1 = Image.open("IMG.jpg")
img2 = img1.filter(ImageFilter.BLUR) #針對影像作模糊化
img2.save("out1.jpg")


img3 = img1.filter(ImageFilter.CONTOUR)#針對影像做輪廓結果
img3.save("out2.jpg")

img4 = img1.filter(ImageFilter.DETAIL)#針對影像做細節處理
img4.save("out3.jpg")

#關於影像卷積(Convolution)
