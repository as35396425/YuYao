from PIL import Image
from PIL import ImageFilter
'''
img1 = Image.open("IMG.jpg")
img2 = img1.filter(ImageFilter.BLUR) #針對影像作模糊化
img2.save("out1.jpg")


img3 = img1.filter(ImageFilter.CONTOUR)#針對影像做輪廓結果
img3.save("out2.jpg")

img4 = img1.filter(ImageFilter.DETAIL)#針對影像做細節處理
img4.save("out3.jpg")



img5 = img1.filter(ImageFilter.EDGE_ENHANCE) #針對影像做物件邊緣的增強
img5.save("out4.jpg")

img6 = img1.filter(ImageFilter.EDGE_ENHANCE_MORE) #上面濾鏡的MORE
img6.save("out5.jpg")

img7 = img1.filter(ImageFilter.EMBOSS) #浮雕濾鏡
img7.save("out6.jpg")

img8 = img1.filter(ImageFilter.FIND_EDGES)#可以用在品管，做電子元件的良率檢測，邊緣檢測
img8.save("out7.jpg")


#只要是看起來完整的東西叫做物件，所以通常會說對物件的邊緣做增強之類的
#以圖找圖，把裡面的物件切完，然後去找是否特徵相符
img9 = img1.filter(ImageFilter.SMOOTH)  #平滑效果
img9.save("out8.jpg")

img_sharp = img1.filter(ImageFilter.SHARPEN)
img_sharp.save("out9.jpg")


#關於影像卷積(Convolution)
'''
l=[]
print(type(l))