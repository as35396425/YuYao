from math import exp
from tkinter import * 
import random
import tkinter as tk

x = 0

def generate_rand():
    global x
    x=random.randint(0,50000)
    label1.config(text=x)


#設定windos
windos = Tk()
windos.title("test in class")
windos.geometry("800x600+300+200")  #開啟視窗600x400尺寸 ， 開啟位置在(300 200)
windos.config(bg = "gray" )  #bg = 背景顏色


'''
#設定畫布
backG = Canvas(windos,width=450,height=300)  #新增一個畫布物件 寬450高300
img = tk.PhotoImage(file="img.gif")  #畫布只能用gif檔
backG.create_image(250,280,image=img)  #250 280 為偏移值，依照給定的座標進行圖片的偏移
backG.pack(side="left",fill="x",expand=1)
'''

#都是label
label1 = Label(windos,width=20 ,height=10 , text= 0,bg="white" )
label1.pack()


#-------分隔-------

#都是按鈕
btrand = Button(windos ,width=20 ,height=10, text="random" , command=generate_rand,bg="#C2C287") #產生單個亂數值
btrand.pack()

        
btexit = Button(windos ,width=20 ,height=10, text = "Exit" , command=windos.destroy,bg="#C2C287") #破壞掉視窗
btexit.pack()



windos.mainloop() #開啟視窗

