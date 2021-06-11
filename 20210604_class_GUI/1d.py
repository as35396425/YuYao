from math import exp
from tkinter import * 
import random
import tkinter as tk

x = 0
def add():
    global x 
    x+=1
    label1.config(text=x)

def sub():
    global x 
    x-=1
    label1.config(text=x)



#設定windos
windos = Tk()
windos.title("test in class")
windos.geometry("800x600+300+200")  #開啟視窗800x600尺寸 ， 開啟位置在(300 200)
windos.config(bg = "gray" )  #bg = 背景顏色


'''
#設定畫布
backG = Canvas(windos,width=450,height=300)  #新增一個畫布物件 寬450高300
img = tk.PhotoImage(file="img.gif")  #畫布只能用gif檔
backG.create_image(250,280,image=img)  #250 280 為偏移值，依照給定的座標進行圖片的偏移
backG.pack(side="left",fill="x",expand=1)
'''

#都是label
label1 = Label(windos ,width=20 ,height=10, text= 0,bg="white" )
label1.pack()

btadd = Button(windos ,width=20 ,height=10, text = "add" , command=add,bg="orange" ) # +1
btadd.pack()  #按鍵需打包

btsub = Button(windos ,width=20 ,height=10, text = "Sub" , command=sub,bg="orange")# -1
btsub.pack()
        
btexit = Button(windos ,width=20 ,height=10, text = "Exit" , command=windos.destroy,bg="orange") #破壞掉視窗
btexit.pack()




windos.mainloop() #開啟視窗

