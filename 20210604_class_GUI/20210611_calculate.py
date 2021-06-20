import tkinter as tk
from tkinter import *
from tkinter.constants import COMMAND, NSEW
from tkinter.font import Font, families
from typing import Text


L=""
L1=""
ll=[]
c = 0
sum1=""

def clearr(): #簡而言之，把所有用到的全域變數設回初始值
    global c ,L,L1,ll,sum1

    L=""
    L1=""
    ll=[]
    c = 0
    sum1=""
    la.config(text = L)

def dela():  #思路  何時會c==0 輸入數字時  故可以消去
    global c ,L,L1,ll,sum1

    if c==0:
        L=L[0:-1]#不要最後一個 ，所以指定到-1
        la.config(text = L)


def ch(x):  #輸入數字
    global c ,L,L1,ll,sum1


    if len(L)<20 :#根據windows
        L+=x
        la.config(text = L)
        if c == 1:#若上次做完運算的動作，即可近來此流程   簡要: 不用+=了  把當前的運算覆蓋掉(別怕 有存進(ll)list)，"空的" + x
            c = 0  #變回輸入數字模式，免得發生bug  ex倒退指令的判斷
            L=""+x
            la.config(text = L)
            
def op(y):  #運算子
    global c ,L,L1,ll,sum1

    if L !="" and c == 0 or len(ll)==0 :  #空 的當前運算不須用運算子  需要 c在數字模式 才可使用(才不會有++或-- **等情況)
        if y != "=":                      #len(ll)==0 為了讓計算完"="而產出的數字可以直接加運算子 設list的長度等於0也可以進去判斷  因為做完 "=" 會清空記憶體(list)
            L+=y 
            la.config(text= L)
            ll.append(L)
            c=1
        
        elif len(ll)>=1 and y == "=":  #等於符號運算思路  判斷傳回的str is True  and  ram len need >= 1 bcz len(ram) +1 's condition is use operate(+-*/)
            c=1 #set operation's member so c=1  (oper_mode)
            ll.append(L) #將純數字字串append ll_list
            
            for i in ll:  #list 一一拉出物件
                sum1+=i   #給sum1  變成一整串字串
            #print(sum1)
            print("{}={}".format(sum1,eval(sum1)))
            la.config(text= eval(sum1))
            L = str(eval(sum1)) #把結果給予L  ex放在桌上的概念
            sum1 = "" #set initial val
            ll=[]     #同上 清空櫃子  因為櫃子的東西都在桌上用完了 
            print(L)
            

if __name__ == "__main__":
    
    root = Tk()
    root.geometry("600x600+200+100")
    root.title = ("calculator")
    #切豆腐或切出櫃子的概念 ， 矩陣類型的空間，切記寬高會跟著物件一起變，建議下次自己做先用frame分割好畫面
    root.rowconfigure(0,w=2)   #放在大的  set row,col = 0,0 and 比例為2
    root.columnconfigure(0,w=2)  #configure 會一起縮放

    root.rowconfigure(1,w=2)
    root.columnconfigure(1,w=2)

    root.rowconfigure(2,w=2)
    root.columnconfigure(2,w=2)


    root.columnconfigure(3,w=1)
    root.rowconfigure(3,w=1)

    root.rowconfigure(4,w=1)


    div1 = Frame(root,background="#02C874")#宣告物件時就需要宣告在哪裡使用了，我們將FRAME宣告在ROOT當中
    div1.columnconfigure(0,w=1)  #若使用Frame製作模板，記得configure,分配某欄位給FRAME使用，可以想像成在WINDOS裡製作WINDOS
    div1.columnconfigure(1,w=3)
    div1.grid(row=4,column=0,columnspan=4,rowspan=5,sticky=NSEW)


    backG = Canvas(div1,width=450,height=300)  #新增一個畫布物件 寬450高300
    img = tk.PhotoImage(file="img.gif")  #畫布只能用gif檔
    backG.create_image(230,280,image=img)  #250 280 為偏移值，依照給定的座標進行圖片的偏移
    backG.grid(row = 1 , column= 0 , sticky=NSEW)


    la = Label(div1, text="輸入內容",width=25,height=5,font=("Time",20),bg="#DFFFDF") #顯示畫面，把他放進去div1 就不用怕物件因變寬而導致整行變寬
    la.grid(row = 0,column=0, sticky=NSEW)                                  #也是因為在div1中 column有span  所以div1中只有一行


    #由北到南   #簡而言之 排版
    b_00 = Button(root,text="1",command=lambda:ch('1'))
    b_00.grid(row=0,column=0 ,sticky=NSEW)

    b_10 = Button(root,text="4",command=lambda:ch('4'))
    b_10.grid(row=1,column=0,sticky=NSEW)

    b_20 = Button(root,text="7",command=lambda:ch('7'))
    b_20.grid(row=2,column=0,sticky=NSEW)

    b_01 = Button(root,text="2",command=lambda:ch('2'))
    b_01.grid(row=0,column=1,sticky=NSEW)

    b_11 = Button(root,text="5",command=lambda:ch('5'))
    b_11.grid(row=1,column=1,sticky=NSEW)

    b_21 = Button(root,text="8",command=lambda:ch('8'))
    b_21.grid(row=2,column=1,sticky=NSEW)

    b_02 = Button(root,text="3",command=lambda:ch('3'))
    b_02.grid(row=0,column=2,sticky=NSEW)

    b_12 = Button(root,text="6",command=lambda:ch('6'))
    b_12.grid(row=1,column=2,sticky=NSEW)

    b_22 = Button(root,text="9",command=lambda:ch('9'))
    b_22.grid(row=2,column=2,sticky=NSEW)  



    b_plus = Button(root , text="+",command = lambda:op("+")).grid(row=0 , column=3,sticky=NSEW)
    b_sub= Button(root , text="-",command = lambda:op("-")).grid(row=1 , column=3,sticky=NSEW)
    b_muti = Button(root , text="x",command = lambda:op("*")).grid(row=2 , column=3,sticky=NSEW)
    b_di= Button(root , text="/",command = lambda:op("/")).grid(row=3 , column=3,sticky=NSEW)
    b_danyu= Button(root , text="=",command = lambda:op("=")).grid(row=3 , column=2,sticky=NSEW)
    b_clear= Button(root , text="c",command = lambda:clearr()).grid(row=3 , column=3,sticky=NSEW)
    b_del= Button(root , text="<-",command = lambda:dela()).grid(row=3 , column=1,sticky=NSEW)



    root.mainloop()