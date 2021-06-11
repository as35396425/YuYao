from math import exp
from tkinter import * 
import random
import tkinter as tk

x = 0

def generate_rand_notR():
    global label2

    randlist=[]
    while len(randlist) < 6:
        y=random.randint(1,43)
        if y not in randlist:   
            randlist.append(y) 
    
    #都是label----------------------
    label2.config(text=randlist[0])
    label3.config(text=randlist[1])
    label4.config(text=randlist[2])
    label5.config(text=randlist[3])
    label6.config(text=randlist[4])
    label7.config(text=randlist[5])
    #-------------------------------

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

#-----------------------------------------------------
label2 = Label(windos,text="rand1" , bg = "#2894FF" )#
label3 = Label(windos,text="rand2" , bg = "#2894FF" )#
label4 = Label(windos,text="rand3" , bg = "#2894FF" )#
label5 = Label(windos,text="rand5" , bg = "#2894FF" )#
label6 = Label(windos,text="rand6" , bg = "#2894FF" )#
label7 = Label(windos,text="rand6" , bg = "#2894FF" )#
#-----------------------------------------------------
label2.pack()#
label3.pack()#
label4.pack()#
label5.pack()#
label6.pack()#
label7.pack()#
#--------------------




#-------分隔-------

#都是按鈕

        
btexit = Button(windos , text = "Exit" , command=windos.destroy) #破壞掉視窗
btexit.pack()



btrand_notR = Button(windos , text="not repeat rand",command=generate_rand_notR)#產生不重複亂數6個
btrand_notR.pack()



windos.mainloop() #開啟視窗

