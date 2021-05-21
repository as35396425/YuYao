#如何讀入image
import numpy as np
from PIL import Image
from numpy import asarray
from matplotlib import pyplot as plt


image = Image.open("183114369_4395922603770853_2151563024614600667_n.jpg")
data=asarray(image)  #使用asarray 如果讀入來源是np中的，發生改變，此宣告變數也會發生改變

imagex = Image.new("RGB",(255,255),color=(255,0,0))  #自己做一張新的圖片，new("mode",size,color=())
#print(imagex,"\n\n")  會跑出圖片格式  <PIL.Image.Image image mode=RGB size=255x255 at 0x1B9B3C7CFD0> 
datax=np.array(imagex)  #將上述圖片轉換成矩陣資料
datax.setflags(write=1) #setflag成可讀寫型態
print(datax) #矩陣資料

for i in range(0,200):  #開始做漸層
    datax[i,20:i,1]=i//2+1
print("漸層矩陣資料\n{}".format(datax)) #顯示做漸層之矩陣資料
w,h=imagex.size  #w,h為原本圖片的size
#image_new = datax.resize(w,h * 2)#新的圖片為，原本伸展的兩倍
#print("這是經過伸展的圖\n{}".format(image_new)) 

imx = Image.fromarray(datax) #將改變過後的矩陣資料，轉回去圖片格式   
plt.figure()#開框
plt.title("imx")

plt.imshow(imx)#顯示哪張圖圖
plt.show()#顯示在框中

print("data array size:",data.shape)
print(data[18:20,11:20,1])



'''
plt.figure("img")
plt.imshow(image)
plt.axis("on")
plt.title("轉轉")
plt.show()
'''


image2=Image.fromarray(data[:,:,1])
data2=(data[:,:,1]//8)#圖片降階

image3=Image.fromarray(data2)

print(data2)
print(image2.mode) #L代表 8位像素  黑白
print(image2.size)  
image2.save("out_1.jpg") #儲存圖片
image3.save("out_2.jpg")
#plt.imshow(image)
#plt.show()



imm=Image.fromarray(data[:,:,2])
d = asarray(imm)

c=0
b=0
n=[[0]*1394]*2048
#n = asarray(n) #如果顯示圖片，跟下面轉換成np無差別
n=np.array(n)
print(d)
for i in range(0,len(data)):#高
    #print(i)
    for j in range(0,len(data[1])):  #寬
        #print(j)
        n[i][j]=(255-d[i][j])  #黑白的圖片 做負片效果
    #print(c,b)
#print(n)

#n=np.array(n)# 在底下轉換成np圖片會變怪,因為將np指定給list，會變成每個高都一起被指定
print(n)

x=Image.fromarray(n)
if x.mode=="I":  # I 32位元
    x=x.convert("RGB")
x.save("out3.jpg")


plt.figure()
plt.title("x")
plt.imshow(n)
plt.show()




