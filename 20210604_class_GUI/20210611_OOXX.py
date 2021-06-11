import tkinter
from tkinter import Button, Tk
from tkinter.constants import NSEW


def P():
    print("o")
x=0
L = [   [None,None,None],
        [None,None,None],
        [None,None,None]    ]

def OOXX_B(L):
    if (L[0][0]==L[0][1]==L[0][2])and L[0] != [None,None,None]:
        print("Winner",str(x%2))
    if (L[1][0]==L[1][1]==L[1][2])and L[1] != [None,None,None]:
        print("Winner",str(x%2))
    if (L[2][0]==L[2][1]==L[2][2])and L[2] != [None,None,None]:
         print("Winner",str(x%2))
    elif (L[0][0] == L[1][1] == L[2][2] ) and (L[0][0] and L[1][1] and L[2][2])!=None :
        print("Winner",str(x%2))
    elif (L[0][2] == L[1][1] == L[2][0] ) and (L[0][2] and L[1][1] and L[2][0])!=None:
        print("Winner",str(x%2))
    elif (L[0][0] == L[1][0] == L[2][0] ) and (L[0][0] and L[1][0] and L[2][0])!=None:
        print("Winner",str(x%2))
    elif (L[0][1] == L[1][1] == L[2][1] ) and (L[0][1] and L[1][1] and L[2][1])!=None:
        print("Winner",str(x%2))
    elif (L[0][2] == L[1][2] == L[2][2] ) and (L[0][2] and L[1][2] and L[2][2])!=None:
        print("Winner",str(x%2))
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

    print(L[0])
    OOXX_B(L)



root = Tk()
root.geometry("600x600+200+100")
root.title = ("Button")
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






root.mainloop()