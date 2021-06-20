from os import name
from tkinter import *
import hashlib

root = Tk()


def login():
    #print('login')
    name_data = in_name.get()
    passw_data = str(in_passw.get())
    if len (name_data)> 0 and len(passw_data)>0:#判斷兩欄位都有填寫
        s_256 = hashlib.sha256()
        s_256.update(passw_data.encode("utf-8"))    #已經取得資料 且編碼為utf8
        hash_data = s_256.hexdigest()
        print(hash_data)

        if name_data == "11" and hash_data =="5515f0912ec4ca5c9537a9c29ed62372869e0f2332c58eb312bd7ca7de850456":  
                                #把帳密寫在程式碼當中，安全性很低，做hash(雜湊函數)
            root.deiconify()  #讓主視窗跳出來                   h3041723
            login_gui.destroy()  #假設帳號密碼是對的 可以關掉登入介面了
        else :
            in_name.delete(0,"end")
            in_passw.delete(0,"end")
    else:
        in_name.delete(0,"end")
        in_passw.delete(0,"end")

def exit():
    login_gui.destroy()
    root.destroy()


root.geometry("600x400+200+100")
root.title("Login")

login_gui = Toplevel(root)
login_gui.geometry("250x150+0+100")

login_gui.columnconfigure(0,w=1)
login_gui.rowconfigure(0,w=1)




f1 = Frame(login_gui,bg="gray")

f1.grid(column=0,row=0,sticky=NSEW)


f1.rowconfigure(0,w=1)
f1.rowconfigure(1,w=1)
f1.columnconfigure(0,w=1)
f1.columnconfigure(1,w=1)



lab_name = Label(f1,text="name",justify=RIGHT, font= ("Times",20))
lab_passw = Label(f1,text="password",justify=RIGHT, font = ("Times", 20))

in_name = Entry(f1)
in_passw = Entry(f1,show="噓")

b_log = Button(f1, text="登入",command=login)
b_exit = Button(f1, text="離開",command=exit)


lab_name.grid(row=0 ,column=0,sticky=NSEW)
lab_passw.grid(row=1 ,column=0,sticky=NSEW)
in_name.grid(row=0,column=1,sticky=NSEW)
in_passw.grid(row=1,column=1,sticky=NSEW)

b_log.grid(row=2,column=0,sticky=NSEW)
b_exit.grid(row=2,column=1,sticky=NSEW)



def P():
    print("o")
x=0
L = [   [None,None,None],
        [None,None,None],
        [None,None,None]    ]

def OOXX_B(L):
    if (L[0][0]==L[0][1]==L[0][2])and L[0] != [None,None,None]:
        print("Winner",str(x//2))
        root.destroy()
    elif (L[1][0]==L[1][1]==L[1][2])and L[1] != [None,None,None]:
        print("Winner",str(x//2))
        root.destroy()
    elif (L[2][0]==L[2][1]==L[2][2])and L[2] != [None,None,None]:
        print("Winner",str(x%2))
        root.destroy()
    elif (L[0][0] == L[1][1] == L[2][2] ) and (L[0][0] and L[1][1] and L[2][2])!=None :
        print("Winner",str(x%2))
        root.destroy()
    elif (L[0][2] == L[1][1] == L[2][0] ) and (L[0][2] and L[1][1] and L[2][0])!=None:
        print("Winner",str(x%2))
        root.destroy()      
    elif (L[0][0] == L[1][0] == L[2][0] ) and (L[0][0] and L[1][0] and L[2][0])!=None:
        print("Winner",str(x%2))
        root.destroy()       
    elif (L[0][1] == L[1][1] == L[2][1] ) and (L[0][1] and L[1][1] and L[2][1])!=None:
        print("Winner",str(x%2))
        root.destroy()      
    elif (L[0][2] == L[1][2] == L[2][2] ) and (L[0][2] and L[1][2] and L[2][2])!=None:
        print("Winner",str(x%2))
        root.destroy()       
    elif x==9:
        root.destroy()


def OOXX(n):
    global x
    if n == "00" and b_00.cget("text")=='2':
        if x%2 == 0:
            b_00.config(text="O")
         
        else:
            b_00.config(text="X")
        L[0][0]=(b_00.cget("text"))           

    if n == '10' and b_10.cget("text")=='2':
        if x%2 == 0:
            b_10.config(text="O")

        else:
            b_10.config(text="X")
        L[1][0] = (b_10.cget("text"))           


    if n == '20'and b_20.cget("text")=='2':
        if x%2 == 0:
            b_20.config(text="O")
        else:
            b_20.config(text="X")
        L[2][0]=(b_20.cget("text"))           

    if n == '01' and b_01.cget("text")=='2':
        if x%2 == 0:
            b_01.config(text="O")
     
        else:
            b_01.config(text="X")
        L[0][1]=(b_01.cget("text"))           

    if n == '11'and b_11.cget("text")=='2':
        if x%2 == 0:
            b_11.config(text="O")
        else:
            b_11.config(text="X")
        L[1][1]=(b_11.cget("text"))           

    if n == '21'and b_21.cget("text")=='2':
        if x%2 == 0:
            b_21.config(text="O")
        else:
            b_21.config(text="X")
        L[2][1]=(b_21.cget("text"))           

    if n == '02' and b_02.cget("text")=='2':
        if x%2 == 0:
            b_02.config(text="O")
        else:
            b_02.config(text="X")
        L[0][2]=(b_02.cget("text"))           

    if n == '12'and b_12.cget("text")=='2':
        if x%2 == 0:
            b_12.config(text="O")
        else:
            b_12.config(text="X")
        L[1][2]=(b_12.cget("text"))           

    if n == '22'and b_22.cget("text")=='2':
        if x%2 == 0:
            b_22.config(text="O")
        else:
            b_22.config(text="X")
        L[2][2]=(b_22.cget("text"))           

    x+=1
    OOXX_B(L)




root.rowconfigure(0,w=1)
root.columnconfigure(0,w=1)

root.rowconfigure(1,w=1)
root.columnconfigure(1,w=1)

root.rowconfigure(2,w=1)
root.columnconfigure(2,w=1)

#由北到南 由西到東
b_00 = Button(root,text="2",command=lambda:OOXX("00"))
b_00.grid(row=0,column=0,sticky=NSEW)

b_10 = Button(root,text="2",command=lambda:OOXX("10"))
b_10.grid(row=1,column=0,sticky=NSEW)

b_20 = Button(root,text="2",comman=lambda:OOXX("20"))
b_20.grid(row=2,column=0,sticky=NSEW)

b_01 = Button(root,text="2",command=lambda:OOXX("01"))
b_01.grid(row=0,column=1,sticky=NSEW)

b_11 = Button(root,text="2",command=lambda:OOXX("11"))
b_11.grid(row=1,column=1,sticky=NSEW)

b_21 = Button(root,text="2",command=lambda:OOXX("21"))
b_21.grid(row=2,column=1,sticky=NSEW)


b_02 = Button(root,text="2",command=lambda:OOXX("02"))
b_02.grid(row=0,column=2,sticky=NSEW)

b_12 = Button(root,text="2",command=lambda:OOXX("12"))
b_12.grid(row=1,column=2,sticky=NSEW)

b_22 = Button(root,text="2",command=lambda:OOXX("22"))
b_22.grid(row=2,column=2,sticky=NSEW)  










root.withdraw() #先把它抽起來，不會同時執行
root.mainloop()



