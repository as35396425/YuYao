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
        #print(hash_data)

        if name_data == "csie" and hash_data =="5515f0912ec4ca5c9537a9c29ed62372869e0f2332c58eb312bd7ca7de850456":  #把帳密寫在程式碼當中，安全性很低，做hash(雜湊函數)
            root.deiconify()  #讓主視窗跳出來
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



def eec():   #用列字典方式一一比較
    x=rootin.get()
    d= {
        
        
        'sha256':{      
                    "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4" : '1234',
                    '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8' :"password",
                    'bef57ec7f53a6d40beb640a780a639c83bc29ac8a9816f1fc6c5c6dcd93c4721' :"abcdef",
                    "65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5" :"qwerty"
                    
                    
                    },
        "sha1":{
            
            "1be168ff837f043bde17c0314341c84271047b31" : "1234"   ,
            "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8":"password" ,
            "1f8ac10f23c5b5bc1167bda84b833e5c057a77d2":"abcdef"   ,
            "b1b3773a05c0ed0176787a4f1574ff0075f7521e":"qwerty"   ,
                
                
                },
        "md5":{
            
            "81dc9bdb52d04dc20036dbd8313ed055" : "1234"   ,
            "5f4dcc3b5aa765d61d8327deb882cf99":"password" ,
            "e80b5017098950fc58aad83c8c14978e":"abcdef"   ,
            "d8578edf8458ce06fbc5bb76a58c5ca4":"qwerty"   ,   
                }
        }
    
    if len(x)>0:
        outP=""
        
        for i in d:
            for j in d[i]:
                #print(j ,d[i][j])
                
                if x == j:
                    outP = "{}方法加密 原始數據:{}".format(i,d[i][j])
                    rootlabel.config(text=outP)


        if outP == "":
                    rootlabel.config(text='不在加密庫')

    else:
        rootlabel.config(text="請輸入數字")


root.geometry("600x400+200+100")
root.title("Login")

login_gui = Toplevel(root)
login_gui.geometry("450x350+0+100")



login_gui.columnconfigure(0,w=1)
login_gui.columnconfigure(1,w=2)
login_gui.rowconfigure(0,w=1)

f1 = Frame(login_gui,bg="gray")
f1.grid(column=0,row=0,sticky=NSEW)



lab_name = Label(f1,anchor=E,text="name",justify=RIGHT, font = ("Times",20))
lab_passw = Label(f1,anchor=E,text="password",justify=RIGHT, font = ("Times", 20))

in_name = Entry(f1)
in_passw = Entry(f1,show="#")

b_log = Button(f1, text="登入",command=login)
b_exit = Button(f1, text="離開",command=exit)


lab_name.grid(row=0 ,column=0,sticky=NSEW)
lab_passw.grid(row=1 ,column=0,sticky=NSEW)
in_name.grid(row=0,column=1,sticky=NSEW)
in_passw.grid(row=1,column=1,sticky=NSEW)

b_log.grid(row=2,column=0,sticky=NSEW)
b_exit.grid(row=2,column=1,sticky=NSEW)


root.columnconfigure(0,w=1)
root.columnconfigure(1,w=1)
root.rowconfigure(0,w=1)
root.rowconfigure(1,w=1)


rootin = Entry(root)
rootin.grid(row=0,column=0)

rootButton = Button(root,text="執行",command=lambda:eec())
rootButton.grid(row=1,column=0)

rootButton_exit = Button(root,text="離開",command=exit)
rootButton_exit.grid(row=1,column=1)


rootlabel = Label(root,text="display")
rootlabel.grid(row=0,column=1)





root.withdraw() #先把它抽起來，不會同時執行
root.mainloop()



