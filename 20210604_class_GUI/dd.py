import tkinter
from tkinter import Button, Label, Tk
from tkinter.constants import NSEW
from typing import Text



def ch(x):
    print(x)



root = Tk()
root.geometry("600x600+200+100")
root.title = ("Button")
root.rowconfigure(0,w=1)
root.columnconfigure(0,w=1)

root.rowconfigure(1,w=1)
root.columnconfigure(1,w=1)

root.rowconfigure(2,w=1)
root.columnconfigure(2,w=1)
root.rowconfigure(3,w=1)

la = Label(root , text="55555")
la.grid(row=3,column=0)


#由北到南 由西到東
b_00 = Button(root,text="1",command=lambda:ch(Button.cget('text')))
b_00.grid(row=0,column=0,sticky=NSEW )

b_10 = Button(root,text="4")
b_10.grid(row=1,column=0,sticky=NSEW)

b_20 = Button(root,text="7")
b_20.grid(row=2,column=0,sticky=NSEW)

b_01 = Button(root,text="2")
b_01.grid(row=0,column=1,sticky=NSEW)

b_11 = Button(root,text="5")
b_11.grid(row=1,column=1,sticky=NSEW)

b_21 = Button(root,text="8")
b_21.grid(row=2,column=1,sticky=NSEW)


b_02 = Button(root,text="3")
b_02.grid(row=0,column=2,sticky=NSEW)

b_12 = Button(root,text="6")
b_12.grid(row=1,column=2,sticky=NSEW)

b_22 = Button(root,text="9")
b_22.grid(row=2,column=2,sticky=NSEW)  




root.mainloop()